from flask import Flask, render_template, request
import collectionRetrieval, sortingLarge, parsing

app = Flask(__name__)

#This dictates where page will load
@app.route('/', methods=['GET', 'POST'])
#function name doesn't matter
def index():
    #Load the home page
    return render_template('index.html')

@app.route('/shelfsort', methods=['GET', 'POST'])
def shelfsort():
    if request.method == 'POST':
        collection = collectionRetrieval.collectionRetrieval(request.form['username'])
        sortedCollection = sortingLarge.sortingLarge(collection[0], collection[1])
        sortedCollection = parsing.basicParse(sortedCollection)
        return render_template('shelfsort.html', games=sortedCollection)
    else:
        sortedCollection = [[['Terra Mystica', 'https://cf.geekdo-images.com/thumb/img/VhwSgo7od1i4qGOEyI-PaZPgrmU=/fit-in/200x150/pic1487128.jpg'], ['Terra Mystica: Fire & Ice', 'https://cf.geekdo-images.com/thumb/img/VE_g85F04Bzw07vg15EFo5NfVhk=/fit-in/200x150/pic2227159.png'], ['The 7th Continent', 'https://cf.geekdo-images.com/thumb/img/zj6guxkAq2hrtEbLGFrIPCh4jv0=/fit-in/200x150/pic2648303.jpg'], ['Terraforming Mars', 'https://cf.geekdo-images.com/thumb/img/yFqQ569DfL8NSTGTUw0vF9SCR7k=/fit-in/200x150/pic3536616.jpg']], [['Battlestar Galactica: The Board Game', 'https://cf.geekdo-images.com/thumb/img/NpZjJd2NgxSJV2WrlB_U1e89txY=/fit-in/200x150/pic354500.jpg'], ['Battlestar Galactica: The Board Game – Daybreak Expansion', 'https://cf.geekdo-images.com/thumb/img/cD4HkLWcaWJx-IMuTNE57Gn1gB4=/fit-in/200x150/pic1639528.jpg'], ['Battlestar Galactica: The Board Game – Exodus Expansion', 'https://cf.geekdo-images.com/thumb/img/58f3cQPDZu8rENJV1dCgr44EKIE=/fit-in/200x150/pic834119.jpg'], ['Battlestar Galactica: The Board Game – Pegasus Expansion', 'https://cf.geekdo-images.com/thumb/img/24VuBbBkNd8UYr0whNF-Np1xpp4=/fit-in/200x150/pic512021.jpg']], [['7 Wonders Duel', 'https://cf.geekdo-images.com/thumb/img/cwWMq5feF7O4O82HJOK3WE5IZ6o=/fit-in/200x150/pic3376065.jpg'], ['Gloomhaven', 'https://cf.geekdo-images.com/thumb/img/e7GyV4PaNtwmalU-EQAGecwoBSI=/fit-in/200x150/pic2437871.jpg'], ['War of the Ring (Second Edition)', 'https://cf.geekdo-images.com/thumb/img/ScZ6Zu4wgK9JRqFWUnA89efhT-0=/fit-in/200x150/pic1215633.jpg']], [['Arkham Horror: The Card Game', 'https://cf.geekdo-images.com/thumb/img/66qtunbh0lfNhBrynkLruHyfZeY=/fit-in/200x150/pic3122349.jpg'], ['The Castles of Burgundy', 'https://cf.geekdo-images.com/thumb/img/WQrgUYzyNADux66REz6_rfF26HU=/fit-in/200x150/pic1176894.jpg'], ['Gaia Project', 'https://cf.geekdo-images.com/thumb/img/5P9XdMqgHu8f56SlenLalqSK_GU=/fit-in/200x150/pic3763556.jpg'], ['Twilight Imperium (Fourth Edition)', 'https://cf.geekdo-images.com/thumb/img/UOV5jJadzHc6ebYd5CfZXGbOWsc=/fit-in/200x150/pic3727516.jpg']], [['Great Western Trail', 'https://cf.geekdo-images.com/thumb/img/ojTMe48mgDcQdcrHJ1d_CSLtc7w=/fit-in/200x150/pic3113247.jpg'], ['Star Wars: Rebellion', 'https://cf.geekdo-images.com/thumb/img/OF1Hi31Kq53difqVp0TiBUySl0w=/fit-in/200x150/pic4325841.jpg'], ['Through the Ages: A New Story of Civilization', 'https://cf.geekdo-images.com/thumb/img/Ohqc2KTYdureA4PNjMqLXP4mUlU=/fit-in/200x150/pic2663291.jpg'], ['Viticulture Essential Edition', 'https://cf.geekdo-images.com/thumb/img/sD_qvrzIbvfobJj0ZDAaq-TnQPs=/fit-in/200x150/pic2649952.jpg']], [['Puerto Rico', 'https://cf.geekdo-images.com/thumb/img/pYFq1WbW-LIQCvWCFxjQuDC-nho=/fit-in/200x150/pic158548.jpg'], ['Twilight Struggle', 'https://cf.geekdo-images.com/thumb/img/mEmeJrI3AbGTpWyeFOZnR0s_LcY=/fit-in/200x150/pic361592.jpg'], ['Clank!: Sunken Treasures', 'https://cf.geekdo-images.com/thumb/img/otfXeH_ecim-K6ar97i5UplcXHI=/fit-in/200x150/pic3489154.jpg']], [['Caverna: The Cave Farmers', 'https://cf.geekdo-images.com/thumb/img/5O2lQXD3exl0-K3zKrpIQiWV6qo=/fit-in/200x150/pic1778149.jpg'], ['Concordia', 'https://cf.geekdo-images.com/thumb/img/2h9KB__ig9_BA8yG_GfYug3yXr4=/fit-in/200x150/pic3678983.jpg'], ['Pandemic Legacy: Season 1', 'https://cf.geekdo-images.com/thumb/img/WI5NmPd9C3PpRvHKoP4a0Ettlao=/fit-in/200x150/pic2452831.png'], ['Scythe', 'https://cf.geekdo-images.com/thumb/img/ZpuWhZuKrFry__SY8CTRuQp35rk=/fit-in/200x150/pic3163924.jpg']]]
        return render_template('shelfsort.html', games=sortedCollection)



if __name__ == "__main__":
        app.run()
