from pytest import mark
from dateutil import parser
from django.utils import timezone
from datetime import datetime, timedelta
from players.tests.factories import PlayerFactory
from leagues.tests.factories import CircuitFactory
from matches.tests.factories import MatchFactory
from api.tests.services import BuzzClient

@mark.filterwarnings(
    'ignore:DateTimeField Match.start_time received a naive datetime')
@mark.django_db
def test_get_matches_upcoming(django_app):
    """
    Get all upcmoing matches in next 24 hours
    """
    client = BuzzClient(django_app)
    circuit = CircuitFactory()

    now = timezone.now()
    match_1 = MatchFactory(circuit=circuit, start_time=now + timedelta(hours=2))
    match_2 = MatchFactory(circuit=circuit, start_time=now + timedelta(hours=23))

    # These should not show up in results
    MatchFactory(circuit=circuit, start_time=now + timedelta(hours=26))
    MatchFactory(circuit=circuit, start_time=now - timedelta(hours=1))

    params = 'hours=24'
    resp = client.matches(params)    

    assert resp['count'] == 2

    matches = resp['results']

    # Sort Order
    assert parser.parse(matches[0]['start_time']) < parser.parse(matches[1]['start_time'])
    
    # Basic field presence check
    assert matches[0]['home']['id'] == match_1.home.id
    assert matches[0]['away']['id'] == match_1.away.id
    assert matches[0]['circuit']
    assert matches[0]['round']
    assert 'number' in matches[0]['round'].keys()
    assert 'name' in matches[0]['round'].keys()
    assert matches[0]['start_time']
    assert matches[0]['time_until']
    assert matches[0]['scheduled']

    assert 'primary_caster' in matches[0].keys()
    assert 'secondary_casters' in matches[0].keys()
    assert 'result' in matches[0].keys()
    assert 'vod_link' in matches[0].keys()


@mark.django_db
def test_get_team_matches(django_app):
    """
    Get all upcmoing matches in next 24 hours
    """
    client = BuzzClient(django_app)
    circuit = CircuitFactory()

    now = timezone.now()

    match_1 = MatchFactory(circuit=circuit, start_time=now - timedelta(days=2))
    team = match_1.home 
    
    match_2 = MatchFactory(
        circuit=circuit, away=team, start_time=now + timedelta(hours=2)) 
    match_3 = MatchFactory(
        circuit=circuit, home=team, start_time=now + timedelta(days=8))
    match_4 = MatchFactory(
        circuit=circuit, away=team, start_time=now + timedelta(days=17))

    # These should not show up in results
    MatchFactory(circuit=circuit, start_time=now + timedelta(hours=26))
    MatchFactory(circuit=circuit, start_time=now - timedelta(hours=1))

    params = f'team={team.name}&league={circuit.season.league.name}&season={circuit.season.name}'
    resp = client.matches(params)    

    assert resp['count'] == 4

@mark.django_db
def test_get_matches_starts_in_minutes(django_app):
    """
    Get matches starting in the next n minutes
    """
    client = BuzzClient(django_app)
    circuit = CircuitFactory()

    now = timezone.now()

    match = MatchFactory(circuit=circuit, start_time=now + timedelta(minutes=5))
    
    MatchFactory(
        circuit=circuit, start_time=now + timedelta(minutes=7)) 

    MatchFactory(
        circuit=circuit, start_time=now - timedelta(minutes=1))

    params = 'starts_in_minutes=5'
    resp = client.matches(params)    

    assert resp['count'] == 1

