#!/usr/bin/env python2
# -*-: coding utf-8 -*-
import time

from snipssonos.use_cases.request_objects import InjectEntitiesRequestObject
from snipssonos.helpers.snips_config_parser import read_configuration_file
from snipssonos.services.spotify.spotify_music_custom_service import SpotifyCustomService
from snipssonos.services.injection_service import InjectEntitiesService
from snipssonos.use_cases.inject_entities import InjectEntitiesUseCase

HERMES_HOST = "localhost"
SECONDS_IN_A_DAY = 86400.0
ARTIST_ENTITY_NAME = "snips/artist"

if __name__ == "__main__":
    configuration = read_configuration_file("config.ini")
    client_id = configuration['secret']['client_id']
    client_secret = configuration['secret']['client_secret']
    access_token = configuration['secret']['access_token']

    music_custom_service = SpotifyCustomService(client_id, client_secret, access_token)
    injection_service = InjectEntitiesService(HERMES_HOST)

    # starttime = time.time()

    # Code taken from: https://stackoverflow.com/a/25251804
    # TODO first call iterate with all top data and in the loop just keep getting short term top data
    # TODO: enable loop when refresh_token issue is solved
    # while True:
    inject_entities_request = InjectEntitiesRequestObject(ARTIST_ENTITY_NAME)
    use_case = InjectEntitiesUseCase(music_custom_service, injection_service)

    response = use_case.process_request(inject_entities_request)

    # time.sleep(SECONDS_IN_A_DAY - ((time.time() - starttime) % SECONDS_IN_A_DAY))
