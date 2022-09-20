from rest_framework import serializers

from core.models.profile import Profile


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'race',
            'is_disability',
            'is_veteran',
            'date_of_birth',
            'sexual_orientation',
            'user'
        ]
