# views.py
from rest_framework.generics import ListAPIView
from .models import TrackClone
from .serializers import TrackSerializer
from spotifier.utils import get_top_tracks_of_artist, get_and_save_artist, get_access_token
from spotifier.constants import client_id, client_secret
from .crawler import song_downloader


artists_data =  [
    {
        "name":"the weekend",
        "id": "1Xyo4u8uXC1ZmMpatF05PJ",
        "rank":1
    },
    {
        "name":"ed sheeran",
        "id":"6eUKZXaKkcviH0Ku9w2n3V",
        "rank":2
    },
    {
        "name":"miley cyrus",
        "id":"5YGY8feqx7naU7z4HrwZM6",
        "rank":3
    },
    {
        "name":"taylor swift",
        "id":"06HL4z0CvFAxyc27GXpf02",
        "rank":4
    },
    {
        "name":"shakira",
        "id":"0EmeFodog0BfCgMzAIvKQp",
        "rank":5
    },
    {
        "name":"rihanna",
        "id":"5pKCCKE2ajJHZ9KAiaK11H",
        "rank":6
    },
    {
        "name":"sam smith",
        "id":"2wY79sveU1sp5g7SokKOiI",
        "rank":7
    },
    {
        "name":"david guetta",
        "id":"1Cs0zKBU1kc0i8ypK3B9ai",
        "rank":8
    },
    {
        "name":"sza",
        "id":"7tYKF4w9nC0nq9CsPZTHyP",
        "rank":9
    },
    {
        "name":"drake",
        "id":"3TVXtAsR1Inumwj472S9r4",
        "rank":10
    },
    {
        "name":"justin bieber",
        "id":"1uNFoZAHBGtllmzznpCI3s",
        "rank":11
    },
    {
        "name":"eminem",
        "id":"7dGJo4pcD2V6oG8kP0tJRR",
        "rank":12
    },
    {
        "name":"harry styles",
        "id":"6KImCVD70vtIoJWnq6nGn3",
        "rank":13
    },
    {
        "name":"bad bunny",
        "id":"4q3ewBCX7sLwd24euuV69X",
        "rank":14
    },
    {
        "name":"dua lipa",
        "id":"2ThsBNtjuUEERqcpXQEoYR",
        "rank":15
    },
    {
        "name":"21 savage",
        "id":"1URnnhqYAYcrqrcwql10ft",
        "rank":8
    },
    {
        "name":"coldplay",
        "id":"4gzpq5DPGxSnKTe4SA8HAU",
        "rank":17
    },
    {
        "name":"calvin harris",
        "id":"7CajNmpbOovFoOoasH2HaY",
        "rank":18
    },
    {
        "name":"bruno mars",
        "id":"0du5cEVh5yTK9QJze8zA0C",
        "rank":19
    },
    {
        "name":"imagine dragons",
        "id":"53XhwfbYqKCa1cC15pYq2q",
        "rank":20
    },
    {
        "name":"lady gaga",
        "id":"1HY2Jd0NmPuamShAr6KMms",
        "rank":21
    },
    {
        "name":"bizarrap",
        "id":"716NhGYqD1jl2wI1Qkgq36",
        "rank":22
    },
    {
        "name":"ariana grande",
        "id":"66CXWjxzNUsdJxJ2JdwvnR",
        "rank":23
    },
    {
        "name":"selena gomez",
        "id":"0C8ZW7ezQVs4URX5aX7Kqx",
        "rank":24
    },
    {
        "name":"charis brown",
        "id":"7bXgB6jMjp9ATFy66eO08Z",
        "rank":25
    },
    {
        "name":"maroon 5",
        "id":"04gDigrS5kc9YWfZHwBETP",
        "rank":26
    },
    {
        "name":"beyonce",
        "id":"6vWDO969PvNqNYHIOW5v0m",
        "rank":27
    },
    {
        "name":"doja cat",
        "id":"5cj0lLjcoR7YOSnhnX0Po5",
        "rank":28
    },
    {
        "name":"metro boomin",
        "id":"0iEtIxbK0KxaSlF7G42ZOp",
        "rank":29
    },
    {
        "name":"kanye west",
        "id":"5K4W6rqBFWDnAN6FQUkS6x",
        "rank":30
    },
    {
        "name":"post malone",
        "id":"246dkjvS1zLTtiykXe5h60",
        "rank":31
    },
    {
        "name":"billie eilish",
        "id":"6qqNVTkY8uBg9cP3Jd7DAH",
        "rank":32
    },
    {
        "name":"adele",
        "id":"4dpARuHxo51G3z768sgnrY",
        "rank":33
    },
    {
        "name":"bebe rexha",
        "id":"64M6ah0SkkRsnPGtGiRAbb",
        "rank":34
    },
    {
        "name":"khalid",
        "id":"6LuN9FCkKOj5PcnpouEgny",
        "rank":35
    },
    {
        "name":"katy perry",
        "id":"6jJ0s89eD6GaHleKKya26X",
        "rank":36
    },
    {
        "name":"j balvin",
        "id":"1vyhD5VmyZ7KMfW5gqLgo5",
        "rank":37
    },
    {
        "name":"onerepublic",
        "id":"5Pwc4xIPtQLFEnJriah9YJ",
        "rank":38
    },
    {
        "name":"elton john",
        "id":"3PhoLpVuITZKcymswpck5b",
        "rank":39
    },
    {
        "name":"daddy yankee",
        "id":"4VMYDCV2IEDYJArk749S6m",
        "rank":40
    },
    {
        "name":"ozuna",
        "id":"1i8SpTcr7yvPOmcqrbnVXY",
        "rank":41
    },
    {
        "name":"kim petras",
        "id":"3Xt3RrJMFv5SZkCfUE8C1J",
        "rank":42
    },
    {
        "name":"future",
        "id":"1RyvyyTE3xzB2ZywiAwp0i",
        "rank":43
    },
    {
        "name":"tiesto",
        "id":"2o5jDhtHVPhrJdv3cEQ99Z",
        "rank":44
    },
    {
        "name":"sia",
        "id":"5WUlDfRSoLAfcVSX1WnrxN",
        "rank":45
    },
    {
        "name":"shawn mendes",
        "id":"7n2wHs1TKAczGzO7Dd2rGr",
        "rank":46
    },
    {
        "name":"th kid laroi",
        "id":"2tIP7SsRs7vjIcLrU85W8J",
        "rank":47
    },
    {
        "name":"travis scott",
        "id":"0Y5tJX1MQlPlqiwlOH1tJY",
        "rank":48
    },

    {
        "name":"queen",
        "id":"1dfeR4HaWDbWqFHLkxsg1d",
        "rank":49
    },

    {
        "name":"nicki minaj",
        "id":"0hCNtLu0JehylgoiP8L4Gh",
        "rank":50
    },
    {
        "name":"kendrick lamar",
        "id":"2YZyLoL8N0Wb9xBt1NhZWg",
        "rank":51
    },
    {
        "name":"rauw alejandro",
        "id":"1mcTU81TzQhprhouKaTkpq",
        "rank":52
    },
    {
        "name":"marshmello",
        "id":"64KEffDW9EtZ1y2vBYgq8T",
        "rank":53
    },
    {
        "name":"halsey",
        "id":"26VFTg2z8YR0cCuwLzESi2",
        "rank":54
    },
    {
        "name":"arctic monkeys",
        "id":"7Ln80lUS6He07XvHI8qqHH",
        "rank":55
    },
    {
        "name":"rosalia",
        "id":"7ltDVBr6mKbRvohxheJ9h1",
        "rank":56
    },
    {
        "name":"black eyed peas",
        "id":"1yxSLGMDHlW21z4YXirZDS",
        "rank":57
    },
    {
        "name":"camila cabello",
        "id":"4nDoRrQiYLoBzwC5BhVJzF",
        "rank":58
    },
    {
        "name":"karol g",
        "id":"790FomKkXshlbRYZFtlgla",
        "rank":59
    },
    {
        "name":"lana del rey",
        "id":"00FQb4jTyendYWaN8pK0wa",
        "rank":60
    },
    {
        "name":"rema",
        "id":"46pWGuE3dSwY3bMMXGBvVS",
        "rank":61
    },
    {
        "name":"meghan trainor",
        "id":"6JL8zeS1NmiOftqZTRgdTz",
        "rank":62
    },
    {
        "name":"lil nas x",
        "id":"7jVv8c5Fj3E9VhNjxT4snq",
        "rank":63
    },
    {
        "name":"bts",
        "id":"3Nrfpe0tUJi4K4DXYWgMUX",
        "rank":64
    },
    {
        "name":"raye",
        "id":"5KKpBU5eC2tJDzf0wmlRp2",
        "rank":65
    },
    {
        "name":"charlie puth",
        "id":"6VuMaDnrHyPL1p4EHjYLi7",
        "rank":66
    },
    {
        "name":"one direction",
        "id":"4AK6F7OLvEQ5QYCBNiQWHq",
        "rank":67
    },
    {
        "name":"xxxtentacion",
        "id":"15UsOTVnJzReFVN1VCnxy4",
        "rank":68
    },
    {
        "name":"robin schulz",
        "id":"3t5xRXzsuZmMDkQzgOX35S",
        "rank":69
    },
    {
        "name":"feid",
        "id":"2LRoIwlKmHjgvigdNGBHNo",
        "rank":70
    },
    {
        "name":"p!nk",
        "id":"1KCSPY1glIKqW2TotWuXOR",
        "rank":71
    },
    {
        "name":"olivia rodrigo",
        "id":"1McMsnEElThX1knmY4oliG",
        "rank":72
    },
    {
        "name":"oliver tree",
        "id":"6TLwD7HPWuiOzvXEa3oCNe",
        "rank":73
    },
    {
        "name":"manuel turizo",
        "id":"0tmwSHipWxN12fsoLcFU3B",
        "rank":74
    },
    {
        "name":"jay-z",
        "id":"3nFkdlSjzX9mRTtwJOzDYB",
        "rank":75
    },
    {
        "name":"michael jackson",
        "id":"3fMbdgg4jU18AjLCKBhRSm",
        "rank":76
    },
    {
        "name":"linkin park",
        "id":"6XyY86QOPPrYVGvF9ch6wz",
        "rank":77
    },
    {
        "name":"nicki minaj",
        "id":"0hCNtLu0JehylgoiP8L4Gh",
        "rank":78
    },
    {
        "name":"quevedo",
        "id":"52iwsT98xCoGgiGntTiR7K",
        "rank":79
    },
    {
        "name":"lil uzi vert",
        "id":"4O15NlyKLIASxsJ0PrXPfz",
        "rank":80
    },
    {
        "name":"maluma",
        "id":"1r4hJ1h58CWwUQe3MxPuau",
        "rank":81
    },
    {
        "name":"the chainsmokers",
        "id":"69GGBxA162lTqCwzJG5jLp",
        "rank":82
    },
    {
        "name":"avicii",
        "id":"1vCWHaC5f2uS3yhpwWbIA6",
        "rank":83
    },
    {
        "name":"stephen sanchez",
        "id":"5XKFrudbV4IiuE5WuTPRmT",
        "rank":84
    },
    {
        "name":"james arthur",
        "id":"4IWBUUAFIplrNtaOHcJPRM",
        "rank":85
    },
    {
        "name":"miguel",
        "id":"360IAlyVv4PCEVjgyMZrxK",
        "rank":86
    },
    {
        "name":"ellie goulding",
        "id":"0X2BH1fck6amBIoJhDVmmJ",
        "rank":87
    },
    {
        "name":"the neighbourhood",
        "id":"77SW9BnxLY8rJ0RciFqkHh",
        "rank":88
    },
    {
        "name":"tate mcrae",
        "id":"45dkTj5sMRSjrmBSBeiHym",
        "rank":89
    },
    {
        "name":"jason derulo",
        "id":"07YZf4WDAMNwqr4jfgOZ8y",
        "rank":90
    },
    {
        "name":"pitbull",
        "id":"0TnOYISbd1XYRBk9myaseg",
        "rank":91
    },
    {
        "name":"britney spears",
        "id":"26dSoYclwsYLMAKD3tpOr4",
        "rank":92
    },
    {
        "name":"ava max",
        "id":"4npEfmQ6YuiwW1GpUmaq3F",
        "rank":93
    },
    {
        "name":"070 shake",
        "id":"12Zk1DFhCbHY6v3xep2ZjI",
        "rank":94
    },
    {
        "name":"myke towers",
        "id":"7iK8PXO48WeuP03g8YR51W",
        "rank":95
    },
    {
        "name":"lewis capaldi",
        "id":"4GNC7GD6oZMSxPGyXy4MNB",
        "rank":96
    },
    {
        "name":"d4vd",
        "id":"5y8tKLUfMvliMe8IKamR32",
        "rank":97
    },
    {
        "name":"juice wrld",
        "id":"4MCBfE4596Uoi2O4DtmEMz",
        "rank":98
    },
    {
        "name":"cardi b",
        "id":"4kYSro6naA4h99UJvo89HB",
        "rank":99
    },
    {
        "name":"j. cole",
        "id":"6l3HvQ5sa6mXTsMTB19rO5",
        "rank":100
    }
]



def get_json_data():
    array_code_artists = []
    for artist in artists_data:
        array_code_artists.append(artist['id'])
    return array_code_artists


class TopTracksOfArtist_first(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[0:25]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks

class TopTracksOfArtist_second(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[25:50]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks

class TopTracksOfArtist_third(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[50:75]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks

class TopTracksOfArtist_forth(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[75:100]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks
    
class DownloaderSong(ListAPIView):
    serializer_class = TrackSerializer
        
    def get_queryset(self):
        list_tracks = TrackClone.objects.all()
        for track in list_tracks:
            song_downloader("https://open.spotify.com/track/"+str(Track.spotify_id))
        