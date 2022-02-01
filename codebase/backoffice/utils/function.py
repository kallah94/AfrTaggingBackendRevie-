import datetime
import json
import time

from backoffice.models import Player, Contract, Period, Country, Team, Staff
from backoffice.utils.mapper import ContractTemplate, PlayerTemplate, CountryTemplate, TeamTemplate, StaffTemplate
import ffmpeg
import subprocess
import uuid

from django.http import QueryDict
from rest_framework import parsers


def player_maker(row, country: Country):
    player = Player()
    player_struct = PlayerTemplate()
    player.last_name = row[player_struct.last_name]
    player.first_name = row[player_struct.first_name]
    player.status = "field_player" if (row[player_struct.role] == "Joueur") else "goal_keeper"
    player.number = row[player_struct.number]
    player.age = row[player_struct.age]
    player.country = country
    Player.save(player)
    return player


def staff_maker(row, country: Country):
    staff = Staff()
    staff_struct = StaffTemplate()
    staff.last_name = row[staff_struct.last_name]
    staff.first_name = row[staff_struct.first_name]
    staff.age = row[staff_struct.age]
    staff.status = "coach" if (row[staff_struct.role] == "Entraineur") else "assistant"
    staff.country = country
    Staff.save(staff)
    return staff


def country_maker(row):
    country_struct = CountryTemplate()
    try:
        country = Country.objects.get(name=row[country_struct.country])
        return country
    except:
        country = Country()
        country.name = row[country_struct.country]
        Country.save(country)
        return country


def team_maker(row):
    team_struct = TeamTemplate()
    try:
        team = Team.objects.get(name=row[team_struct.team_name])
        return team
    except:
        team = Team()
        team.name = row[team_struct.team_name]
        Team.save(team)
        return team


def period_maker(row, player, team):
    period = Period()
    contract_struct = ContractTemplate()
    period.begin = row[contract_struct.begin_contract]
    period.end = row[contract_struct.end_contract]
    period.status = "in_progress" if (row[contract_struct.status_contract] == "en cours") else "finished"
    period.player = player
    period.team = team
    Period.save(period)
    return None


def contract_maker(row, staff, team):
    contract = Contract()
    contract_struct = ContractTemplate()
    contract.begin = row[contract_struct.begin_contract]
    contract.end = row[contract_struct.end_contract]
    contract.status = "in_progress" if (row[contract_struct.status_contract] == "en cours") else "finished"
    contract.staff = staff
    contract.team = team
    Contract.save(contract)
    return None


def make_video(source_url, video_start, video_end):
    subpath = "videos/actions/{}/{}/{}".format(datetime.date.today().year,
                                               datetime.date.today().month,
                                               datetime.date.today().day)
    try:
        subprocess.check_call(['ls', "media/{}".format(subpath)])
    except:
        subprocess.check_call(['mkdir', "media/{}".format(subpath)])
    video_name = uuid.uuid4().hex
    path = "media/{}/{}.mp4".format(subpath, video_name)
    main_video = ffmpeg.input(source_url)
    video = main_video.video.filter('trim', start=video_start, end=video_end).filter('setpts', expr='PTS-STARTPTS')
    audio = main_video.audio.filter('atrim', start=video_start, end=video_end).filter('asetpts', expr='PTS-STARTPTS')
    joined = ffmpeg.concat(video, audio, v=1, a=1).node
    video = joined[0]
    audio = joined[1]
    out_video = ffmpeg.output(video, audio, path)
    out_video.run()

    return "{}/{}.mp4".format(subpath, video_name)


class MultiPartJsonParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = {}
        data = json.loads(result.data["data"])
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        return parsers.DataAndFiles(qdict, result.files)
