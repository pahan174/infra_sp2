from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import CustomUser
from .serializers import (CategorySerializer, CommentSerializer,
                          CreateUserSerializer, GenreSerializer,
                          LoginSerializer, ReviewSerializer,
                          SignUserSerializer, TitleDetailSerializer,
                          TitlesSerializer, GetPersonalAccountSerializers)
from .permissions import AdminOrReadOnly, IsAuthorOrModerOrAdmin

from .filters import TitlesFilter


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    lookup_field = 'username'
    search_fields = ('username',)


@ api_view(['GET', 'PATCH'])
@ permission_classes([IsAuthenticated])
def get_personal_account(request):
    user_id = request.user.pk
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'PATCH':
        serializer = GetPersonalAccountSerializers(user, data=request.data,
                                                   partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    serializer = GetPersonalAccountSerializers(user)
    return Response(serializer.data)


@ api_view(['POST'])
@ permission_classes([AllowAny])
def signup(request):
    serializer = SignUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user = get_object_or_404(CustomUser, username=username)
    confirmation_code = default_token_generator.make_token(user)
    serializer.save(email=email, confirmation_code=confirmation_code)

    send_mail(
        'Тема письма',
        f'Код подтверждения: {confirmation_code}',
        'from@example.com',
        [email],
        fail_silently=False,
    )

    return Response(serializer.data)


@ api_view(['POST'])
@ permission_classes([AllowAny])
def token_login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    confirmation_code = request.data['confirmation_code']
    user = get_object_or_404(CustomUser, username=request.data['username'])
    token = RefreshToken.for_user(user)
    if user.confirmation_code == confirmation_code:
        return Response({'access': str(token.access_token)},
                        status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    lookup_field = 'slug'
    search_fields = ('name',)


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, )
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)


class TitlesViewSet(viewsets.ModelViewSet):
    serializer_class = TitleDetailSerializer
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return TitleDetailSerializer
        return TitlesSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrModerOrAdmin, )
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = self.kwargs.get("title_id")
        new_queryset = Review.objects.filter(title=title)
        return new_queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def perform_destroy(self, instance):
        review = get_object_or_404(Review, id=instance.pk)
        return review.delete()


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrModerOrAdmin, )
    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        new_queryset = Comment.objects.filter(review_id=review_id)
        return new_queryset

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review)
