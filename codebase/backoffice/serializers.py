from abc import ABC, ABCMeta

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'id']


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Attribute
        fields = '__all__'


class AttributeBisSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Attribute
        fields = ['name']


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Manager
        fields = '__all__'


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Action
        fields = '__all__'


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    countryName = serializers.CharField(source='country', read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = League
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    countryName = serializers.CharField(source='country', read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class GameVideoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GameVideo
        fields = '__all__'


class GameSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = '__all__'


class PlayerActionInGameSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    action_name = serializers.CharField(source='action', read_only=True)
    attributes_names = serializers.SlugRelatedField(source='attributes', read_only=True, many=True, slug_field='name')
    player_name = serializers.CharField(source='player', read_only=True)
    team_name = serializers.CharField(source='team', read_only=True)

    class Meta:
        model = PlayerActionInGame
        fields = '__all__'


class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Period
        fields = '__all__'


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Season
        fields = '__all__'


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Contract
        fields = '__all__'


class PlayerPositionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PlayerPosition
        fields = '__all__'


class TeamExcelSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ['file']
