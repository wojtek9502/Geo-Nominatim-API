nominatim_search_response_mock = [
    {"place_id": 4040332, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "relation", "osm_id": 336075, "boundingbox": ["52.0978497", "52.3681531", "20.8516882", "21.2711512"],
     "lat": "52.2319581", "lon": "21.0067249", "display_name": "Warszawa, województwo mazowieckie, Polska",
     "place_rank": 12, "category": "boundary", "type": "administrative", "importance": 0.35001},
    {"place_id": 4034580, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "relation", "osm_id": 2907540, "boundingbox": ["52.0978497", "52.3681531", "20.8516882", "21.2711512"],
     "lat": "52.2337172", "lon": "21.071432235636493", "display_name": "Warszawa, województwo mazowieckie, Polska",
     "place_rank": 14, "category": "boundary", "type": "administrative", "importance": 0.3233433333333333},
    {"place_id": 4036611, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "relation", "osm_id": 336074, "boundingbox": ["52.0978497", "52.3681531", "20.8516882", "21.2711512"],
     "lat": "52.2337172", "lon": "21.071432235636493", "display_name": "Warszawa, województwo mazowieckie, Polska",
     "place_rank": 16, "category": "boundary", "type": "administrative", "importance": 0.29667666666666664},
    {"place_id": 6102668, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "relation", "osm_id": 16078721,
     "boundingbox": ["50.6505991", "50.6554336", "22.6891956", "22.6932478"], "lat": "50.6536111", "lon": "22.6911111",
     "display_name": "Warszawa, Rzeczyce, gmina Frampol, powiat biłgorajski, województwo lubelskie, Polska",
     "place_rank": 20, "category": "boundary", "type": "administrative", "importance": 0.24334333333333333},
    {"place_id": 5862966, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "relation", "osm_id": 13634816, "boundingbox": ["50.4917913", "50.498007", "22.7258755", "22.7301997"],
     "lat": "50.495551", "lon": "22.7278886",
     "display_name": "Warszawa, Korczów, gmina Biłgoraj, powiat biłgorajski, województwo lubelskie, Polska",
     "place_rank": 20, "category": "boundary", "type": "administrative", "importance": 0.24334333333333333},
    {"place_id": 5865892, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "relation", "osm_id": 13634794,
     "boundingbox": ["50.4910455", "50.4936978", "22.6298803", "22.6359032"], "lat": "50.4926202", "lon": "22.6327882",
     "display_name": "Warszawa, Sól, gmina Biłgoraj, powiat biłgorajski, województwo lubelskie, Polska",
     "place_rank": 20, "category": "boundary", "type": "administrative", "importance": 0.24334333333333333},
    {"place_id": 999443, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "node", "osm_id": 3009668396, "boundingbox": ["54.0686131", "54.1086131", "23.1179916", "23.1579916"],
     "lat": "54.0886131", "lon": "23.1379916",
     "display_name": "Warszawa, Żubrówka Stara, gmina Krasnopol, powiat sejneński, województwo podlaskie, Polska",
     "place_rank": 20, "category": "place", "type": "hamlet", "importance": 0.24334333333333333},
    {"place_id": 1031688, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "node", "osm_id": 3009668394, "boundingbox": ["53.9972009", "54.0372009", "22.8585398", "22.8985398"],
     "lat": "54.0172009", "lon": "22.8785398",
     "display_name": "Warszawa, Józefowo, gmina Raczki, powiat suwalski, województwo podlaskie, Polska",
     "place_rank": 20, "category": "place", "type": "hamlet", "importance": 0.24334333333333333},
    {"place_id": 4871465, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "node", "osm_id": 3009668393, "boundingbox": ["53.9476332", "53.9876332", "22.8420236", "22.8820236"],
     "lat": "53.9676332", "lon": "22.8620236",
     "display_name": "Warszawa, Kurianki Pierwsze, gmina Raczki, powiat suwalski, województwo podlaskie, Polska",
     "place_rank": 20, "category": "place", "type": "hamlet", "importance": 0.24334333333333333},
    {"place_id": 4812250, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
     "osm_type": "node", "osm_id": 3009668390, "boundingbox": ["53.2582616", "53.2982616", "22.7964229", "22.8364229"],
     "lat": "53.2782616", "lon": "22.8164229",
     "display_name": "Warszawa, Długołęka, gmina Krypno, powiat moniecki, województwo podlaskie, 19-111, Polska",
     "place_rank": 20, "category": "place", "type": "hamlet", "importance": 0.24334333333333333}]

nominatim_reverse_response_mock = {"place_id": 4032405,
                                   "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                                   "osm_type": "relation", "osm_id": 16128958, "lat": "52.24021205",
                                   "lon": "21.01885200576133",
                                   "display_name": "Kampus Główny UW, Świętokrzyska, Centrum, Śródmieście Północne, Śródmieście, Warszawa, województwo mazowieckie, 00-360, Polska",
                                   "address": {"amenity": "Kampus Główny UW", "road": "Świętokrzyska",
                                               "neighbourhood": "Centrum", "quarter": "Śródmieście Północne",
                                               "suburb": "Śródmieście", "city": "Warszawa",
                                               "state": "województwo mazowieckie", "ISO3166-2-lvl4": "PL-14",
                                               "postcode": "00-360", "country": "Polska", "country_code": "pl"},
                                   "boundingbox": ["52.2370942", "52.2430811", "21.016089", "21.0210742"]}
