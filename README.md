# BDA_Wiki_Projekt
Big Data Analytics Projekt



# Quick start

### Prerequisites:
- Git
- Docker  

Download the repository and navigate to the docker folder.

```shell script
git clone https://github.com/dschork-lab/BDA_Wiki_Projekt && cd BDA_Wiki_Projekt/docker
```

Then start the docker containers via docker compose

```shell script
docker compose up -d
```

Once all the images are downloaded and the containers are started you can access the broker via

```shell script
docker exec -it broker bash
```



### Creating  
```shell script
kafka-topics --create --topic example_topic --zookeeper zookeeper:2181 --partitions 1 --replication-factor 1
```

### Consumer
```shell script
kafka-console-consumer --topic example_topic --bootstrap-server broker:29092 --from-beginning
```

### Producer
```shell script
kafka-console-producer --broker-list broker:29092 --topic example_topic
```
---


Alternatively creating the topics can be done via the UI-Component

Access ``localhost:9000`` and click `+ new` 

---
##Vor Nutzung der Wikipedia Producer Python Datei zu beachten: 

###Zuvor zu installierende Python Dateien:
```shell script
pip install kafka-python
pip install pymongo
pip install requests
```
---

##Wikipedia Guide
### Wikipedia Topic anlegen
```shell script
kafka-topics --create --topic article_information --zookeeper zookeeper:2181 --partitions 1 --replication-factor 1
```

### Consumer & Producer
Python-Dateien ``KafkaMongoDBConnector.py`` und ``WikipediaKafakaConnector.py`` ausführen

### MongoDB Web Interface
Access via ``localhost:8081``

---

##Structure database
Database: article_information  
Collections: changes, id_mood

###changes
Contains the raw changes data from the wikipedia api
```
{
    _id: ObjectId('61963be9818d0995dddcf1e8'),
    id: 1444256956,
    domain: 'en.wikipedia.org',
    timestamp: '2021-11-18T11:41:33Z',
    revision: {
        old: 1055871737,
        'new': 1055884851
    },
    old_version: {
        title: '2021–22 Coupe de France',
        content: 'The 2021–22 Coupe de France is the 105th season of the main football cup competition of France. The competition is organised by the French Football Federation (FFF) and is open to all clubs in French football, as well as clubs from the overseas departments and territories (Guadeloupe, French Guiana, Martinique, Mayotte, New Caledonia, Tahiti, Réunion, Saint Martin, and Saint Pierre and Miquelon).\nThe competition returns largely to the format of 2019–20 after the changes last season due to the COVID-19 pandemic in France. However, on 21 October 2021 it was announced that New Caledonia will not be represented in the competition due to the situation in that territory.\nParis Saint-Germain are the defending champions, after a 2–0 win over Monaco in the 2021 Coupe de France Final.\n\n\nDates\nDates for the first two qualifying round, and any preliminaries required, are set by the individual Regional leagues. From round three, the FFF defines the calendar, with rounds up to and including the round of 32 being scheduled for weekends. The later rounds up to, but not including, the final, taking place on midweek evenings. The final was scheduled for Saturday 8 May 2022.\n\nNotable rule changes\nAfter gaining a second seventh-round spot last season, Mayotte lost it this season, due to the FFF ruling that there were no stadia in the territory of the standard required to host a seventh-round match. The single qualifying team from Mayotte would therefore play its seventh-round match in mainland France.After a DNCG ruling excluding Niort from the 2021–22 competition, only 19 Ligue 2 teams will enter at the seventh-round stage.The number of teams qualifying from each region returned to those of the 2019–20 competition, with adjustments to account for the above two points, i.e. 146 rather than 144 mainland teams will qualify for the seventh round.On 21 October 2021, it was announced that no team from New Caledonia would be present in the seventh round, due to the ongoing COVID-19 pandemic in New Caledonia, and the imposition of lockdown until 31 October 2021.\nTeams\nRound 1 to 6\n\nThe first six rounds, and any preliminaries required, were organised by the Regional Leagues and the Overseas Territories, who allowed teams from within their league structure to enter at any point up to the third round. Teams from Championnat National 3 entered at the third round, those from Championnat National 2 entered at the fourth round and those from Championnat National entered at the fifth round.The number of teams entering at each qualifying round was as follows:\n\n\nRound 7\nThe 146 qualifiers from the Regional Leagues will be joined by the 10 qualifiers from the Overseas Territories and 19 eligible 2021–22 Ligue 2 teams. The qualifiers from Réunion, Martinique, Guadeloupe and French Guiana play off in internal matches.\nLigue 2\n\nRegional Leagues\n\n\nOverseas Territories teams\n\n\nRound 8\nThe winners of the seventh round matches in Guadeloupe and Martinique will play their eighth round matches at home against teams from mainland France. Should the team from Tahiti win their seventh round match, they will also play a home game against a team from mainland France. On 2 November 2021 a draw took place to prioritise the list of National, National 2 and National 3 clubs who had put themselves forward as candidates for overseas travel. The highest prioritised team which qualifies for the eighth round will travel to Guadeloupe, the second highest will travel to Martinique and the third highest will travel to Tahiti if required.\nPriority list of mainland teams\n\nRound of 64\nThe 44 qualifying teams from Round 8 are joined by the 20 2021–22 Ligue 1 teams. 32 ties are drawn in regional groups.\n\nLater rounds\nLater rounds are open draws with no regional grouping.\n\nSeventh round\nDue to there being no New Caledeonia team in the seventh round draw, a mainland team will be awarded a bye to the eighth round.\n\nThe seventh round in Guadeloupe, Martinique, French Guiana and Réunion will take place between the two qualifying teams from each territory, and are pre-drawn by the local league.\nTeams were divided into ten groups, by geography and to ensure the groups are balanced in terms of the levels of the teams. The teams from Tahiti and Mayotte were included in groups E and I respectively. An exempt ball was included in group J.Overseas playoff ties\n\n\n\n\nMain draw\nThe main draw was carried out on 3 November 2021. Ties will be played on 12, 13 and 14 November 2021. Several ties will be played at alternate stadia due to the stadium of the home clubs not being of sufficient standard.\n\nGroup A\n\n\n\n\n\n\n\n\n\n\n\nGroup B\n\n\n\n\n\n\n\n\nGroup C\n\n\n\n\n\n\n\n\nGroup D\n\n\n\n\n\n\n\n\n\nGroup E\n\n\n\n\n\n\n\n\nGroup F\n\n\n\n\n\n\n\n\n\n\n\nGroup G\n\n\n\n\n\n\n\n\nGroup H\n\n\n\n\n\n\n\n\nGroup I\n\n\n\n\n\n\n\n\nGroup J\n\n\n\n\n\n\n\nPD Ergué-Gabéric (6) were drawn as the team given a bye into the eighth round.\n\nEighth round\nThe eighth round draw was pre-determined at the same time as the seventh-round draw. Groupings were carried forward from the seventh round, with the mainland teams travelling for overseas ties replaced by overseas teams that were travelling to the mainland.\nOverseas ties\n\n\nGroup A\n\n\n\n\n\n\nGroup B\n\n\n\n\nGroup C\n\n\n\n\nGroup D\n\n\n\n\nGroup E\n\n\n\n\nGroup F\n\n\n\n\n\n\nGroup G\n\n\n\n\nGroup H\n\n\n\n\nGroup I\n\n\n\n\nGroup J\n\n\n\n\nReferences\n\nExternal links\nOfficial website\n\n\n<!-- \nNewPP limit report\nParsed by mw1361\nCached time: 20211118114137\nCache expiry: 1814400\nReduced expiry: false\nComplications: [vary‐revision‐sha1]\nCPU time usage: 1.834 seconds\nReal time usage: 2.037 seconds\nPreprocessor visited node count: 18457/1000000\nPost‐expand include size: 555849/2097152 bytes\nTemplate argument size: 10197/2097152 bytes\nHighest expansion depth: 12/40\nExpensive parser function count: 0/500\nUnstrip recursion depth: 1/20\nUnstrip post‐expand size: 136846/5000000 bytes\nLua time usage: 0.619/10.000 seconds\nLua memory usage: 6381704/52428800 bytes\nNumber of Wikibase entities loaded: 1/400\n-->\n<!--\nTransclusion expansion time report (%,ms,calls,template)\n100.00% 1297.397      1 -total\n 32.90%  426.888    127 Template:Football_box_collapsible\n 28.15%  365.278     10 Template:Reflist\n 21.10%  273.770     39 Template:Cite_web\n 14.48%  187.889    106 Template:Goal\n  8.80%  114.126      2 Template:Short_description\n  7.99%  103.647     22 Template:Flagicon\n  5.54%   71.875      4 Template:Footballbox_collapsible\n  5.09%   66.021      1 Template:Infobox_football_tournament_season\n  4.63%   60.061      8 Template:Notelist\n-->',
        categories: [
            '2021–22 Coupe de France',
            '2021–22 European domestic association football cups',
            '2021–22 in French football',
            'Articles with short description',
            'CS1 French-language sources (fr)',
            'Coupe de France seasons',
            'Official website not in Wikidata',
            'Short description matches Wikidata'
        ]
    },
    new_version: {
        title: '2021–22 Coupe de France',
        content: 'The 2021–22 Coupe de France is the 105th season of the main football cup competition of France. The competition is organised by the French Football Federation (FFF) and is open to all clubs in French football, as well as clubs from the overseas departments and territories (Guadeloupe, French Guiana, Martinique, Mayotte, New Caledonia, Tahiti, Réunion, Saint Martin, and Saint Pierre and Miquelon).\nThe competition returns largely to the format of 2019–20 after the changes last season due to the COVID-19 pandemic in France. However, on 21 October 2021 it was announced that New Caledonia will not be represented in the competition due to the situation in that territory.\nParis Saint-Germain are the defending champions, after a 2–0 win over Monaco in the 2021 Coupe de France Final.\n\n\nDates\nDates for the first two qualifying round, and any preliminaries required, are set by the individual Regional leagues. From round three, the FFF defines the calendar, with rounds up to and including the round of 32 being scheduled for weekends. The later rounds up to, but not including, the final, taking place on midweek evenings. The final was scheduled for Saturday 8 May 2022.\n\nNotable rule changes\nAfter gaining a second seventh-round spot last season, Mayotte lost it this season, due to the FFF ruling that there were no stadia in the territory of the standard required to host a seventh-round match. The single qualifying team from Mayotte would therefore play its seventh-round match in mainland France.After a DNCG ruling excluding Niort from the 2021–22 competition, only 19 Ligue 2 teams will enter at the seventh-round stage.The number of teams qualifying from each region returned to those of the 2019–20 competition, with adjustments to account for the above two points, i.e. 146 rather than 144 mainland teams will qualify for the seventh round.On 21 October 2021, it was announced that no team from New Caledonia would be present in the seventh round, due to the ongoing COVID-19 pandemic in New Caledonia, and the imposition of lockdown until 31 October 2021.\nTeams\nRound 1 to 6\n\nThe first six rounds, and any preliminaries required, were organised by the Regional Leagues and the Overseas Territories, who allowed teams from within their league structure to enter at any point up to the third round. Teams from Championnat National 3 entered at the third round, those from Championnat National 2 entered at the fourth round and those from Championnat National entered at the fifth round.The number of teams entering at each qualifying round was as follows:\n\n\nRound 7\nThe 146 qualifiers from the Regional Leagues will be joined by the 10 qualifiers from the Overseas Territories and 19 eligible 2021–22 Ligue 2 teams. The qualifiers from Réunion, Martinique, Guadeloupe and French Guiana play off in internal matches.\nLigue 2\n\nRegional Leagues\n\n\nOverseas Territories teams\n\n\nRound 8\nThe winners of the seventh round matches in Guadeloupe and Martinique will play their eighth round matches at home against teams from mainland France. Should the team from Tahiti win their seventh round match, they will also play a home game against a team from mainland France. On 2 November 2021 a draw took place to prioritise the list of National, National 2 and National 3 clubs who had put themselves forward as candidates for overseas travel. The highest prioritised team which qualifies for the eighth round will travel to Guadeloupe, the second highest will travel to Martinique and the third highest will travel to Tahiti if required.\nPriority list of mainland teams\n\nRound of 64\nThe 44 qualifying teams from Round 8 are joined by the 20 2021–22 Ligue 1 teams. 32 ties are drawn in regional groups.\n\nLater rounds\nLater rounds are open draws with no regional grouping.\n\nSeventh round\nDue to there being no New Caledeonia team in the seventh round draw, a mainland team will be awarded a bye to the eighth round.\n\nThe seventh round in Guadeloupe, Martinique, French Guiana and Réunion will take place between the two qualifying teams from each territory, and are pre-drawn by the local league.\nTeams were divided into ten groups, by geography and to ensure the groups are balanced in terms of the levels of the teams. The teams from Tahiti and Mayotte were included in groups E and I respectively. An exempt ball was included in group J.Overseas playoff ties\n\n\n\n\nMain draw\nThe main draw was carried out on 3 November 2021. Ties will be played on 12, 13 and 14 November 2021. Several ties will be played at alternate stadia due to the stadium of the home clubs not being of sufficient standard.\n\nGroup A\n\n\n\n\n\n\n\n\n\n\n\nGroup B\n\n\n\n\n\n\n\n\nGroup C\n\n\n\n\n\n\n\n\nGroup D\n\n\n\n\n\n\n\n\n\nGroup E\n\n\n\n\n\n\n\n\nGroup F\n\n\n\n\n\n\n\n\n\n\n\nGroup G\n\n\n\n\n\n\n\n\nGroup H\n\n\n\n\n\n\n\n\nGroup I\n\n\n\n\n\n\n\n\nGroup J\n\n\n\n\n\n\n\nPD Ergué-Gabéric (6) were drawn as the team given a bye into the eighth round.\n\nEighth round\nThe eighth round draw was pre-determined at the same time as the seventh-round draw. Groupings were carried forward from the seventh round, with the mainland teams travelling for overseas ties replaced by overseas teams that were travelling to the mainland.\nOverseas ties\n\n\nGroup A\n\n\n\n\n\n\nGroup B\n\n\n\n\nGroup C\n\n\n\n\nGroup D\n\n\n\n\nGroup E\n\n\n\n\nGroup F\n\n\n\n\n\n\nGroup G\n\n\n\n\nGroup H\n\n\n\n\nGroup I\n\n\n\n\nGroup J\n\n\n\n\nReferences\n\nExternal links\nOfficial website\n\n\n<!-- \nNewPP limit report\nParsed by mw1361\nCached time: 20211118114137\nCache expiry: 1814400\nReduced expiry: false\nComplications: [vary‐revision‐sha1]\nCPU time usage: 1.834 seconds\nReal time usage: 2.037 seconds\nPreprocessor visited node count: 18457/1000000\nPost‐expand include size: 555849/2097152 bytes\nTemplate argument size: 10197/2097152 bytes\nHighest expansion depth: 12/40\nExpensive parser function count: 0/500\nUnstrip recursion depth: 1/20\nUnstrip post‐expand size: 136846/5000000 bytes\nLua time usage: 0.619/10.000 seconds\nLua memory usage: 6381704/52428800 bytes\nNumber of Wikibase entities loaded: 1/400\n-->\n<!--\nTransclusion expansion time report (%,ms,calls,template)\n100.00% 1297.397      1 -total\n 32.90%  426.888    127 Template:Football_box_collapsible\n 28.15%  365.278     10 Template:Reflist\n 21.10%  273.770     39 Template:Cite_web\n 14.48%  187.889    106 Template:Goal\n  8.80%  114.126      2 Template:Short_description\n  7.99%  103.647     22 Template:Flagicon\n  5.54%   71.875      4 Template:Footballbox_collapsible\n  5.09%   66.021      1 Template:Infobox_football_tournament_season\n  4.63%   60.061      8 Template:Notelist\n-->',
        categories: [
            '2021–22 Coupe de France',
            '2021–22 European domestic association football cups',
            '2021–22 in French football',
            'Articles with short description',
            'CS1 French-language sources (fr)',
            'Coupe de France seasons',
            'Official website not in Wikidata',
            'Short description matches Wikidata'
        ]
    }
}
```

###id_mood
Contains simplified data with mood analysis
```
{
    _id: ObjectId('61963daf22e4ec1dd167071e'),
    id: 1444258541,
    old_revision: 1051438321,
    new_revision: 1055885575,
    old_positive: 608,
    old_negative: 241,
    old_anger: 119,
    old_anticipation: 274,
    old_disgust: 97,
    old_fear: 175,
    old_joy: 249,
    old_sadness: 116,
    old_surprise: 47,
    old_trust: 446,
    new_positive: 608,
    new_negative: 241,
    new_anger: 119,
    new_anticipation: 274,
    new_disgust: 97,
    new_fear: 175,
    new_joy: 249,
    new_sadness: 116,
    new_surprise: 47,
    new_trust: 446,
    old_content_length: 10613,
    new_content_length: 10613
}
```
