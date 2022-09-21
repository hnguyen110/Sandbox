from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.profile import Profile
from core.serializers.profile.base_profile_serializer import BaseProfileSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer = BaseProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile = Profile.objects.filter(user=self.request.user).first()
        if profile is None:
            request.data['user'] = self.request.user.pk
            serializer = BaseProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)
        request.data['user'] = self.request.user.pk
        serializer = BaseProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        profile = get_object_or_404(Profile, user=self.request.user)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
