from rest_framework import serializers
from .models import Team, Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )

    class Meta:
        model = Player
        fields = ('id', 'name', 'team', 'team_id', 'position', 'age', 'injured_resv_list', 'pass_yds', 'rush_yds', 'rec', 'tackles')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    player = PlayerSerializer(
        many=True,
        read_only=True
    )

    team_url = serializers.HyperlinkedIdentityField(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'team_url', 'location', 'division', 'wins', 'losses', 'player')
