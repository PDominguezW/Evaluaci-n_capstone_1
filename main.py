import json

def main():

    # Read data
    tweets = []
    with open('farmers-protest-tweets-2021-03-5.json', ) as f:
        for line in f:
            tweets.append(json.loads(line))

    opcion = 0

    while opcion != 5:

        opcion = get_option()

        if opcion == 1:
            top_retweeted(tweets)
        elif opcion == 2:
            top_usuarios(tweets)
        elif opcion == 3:
            top_dias(tweets)
        elif opcion == 4:
            top_hashtags(tweets)

def get_option():
    print("Seleccione la funcion que desea llamar:")
    print("[1] Los top 10 tweets más retweeted")
    print("[2] Los top 10 usuarios en función de la cantidad de tweets que emitieron")
    print("[3] Los top 10 días donde hay más tweets")
    print("[4] Los top 10 hashtags más usados")
    print("[5] Salir")

    opcion = int(input("Ingrese una opcion: "))
    return opcion

def top_retweeted(data):
    top = ''
    retweeted_count = 0

    for tweet in data:
        if tweet['retweetedCount'] > retweeted_count:
            top = tweet['content']
            retweeted_count = tweet['retweetedCount']

def top_usuarios(data):
    users_count = {}

    for tweet in data:

        # Sumamos si ya esta
        if tweet['user']['username'] in list(users_count.keys()):
            users_count[tweet['user']['username']] += 1
        else:
            users_count[tweet['user']['username']] = 1

    # Ordenamos
    top_users = sorted(users_count.items(), key=lambda x: x[1], reverse=True)

    # Entregamos el top ten
    for i in range(10):
        print(top_users[i])

def top_dias(data):
    pass

def top_hashtags(data):
    pass

if __name__ == '__main__':
    main()