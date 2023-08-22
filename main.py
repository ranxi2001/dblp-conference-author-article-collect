from bs4 import BeautifulSoup

# Read the HTML content
with open("dblp-TPAMI-Volume-45.html", 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
soup

# Let's try to find articles using different tags or classes
article_entries_alternative = soup.find_all('li', class_='entry article')

# Extract titles and first authors using the alternative approach
titles_and_authors_alternative = []
for entry in article_entries_alternative:
    title = entry.find('span', class_='title').text if entry.find('span', class_='title') else None
    authors = entry.find_all('span', itemprop='author')
    first_author = authors[0].text if authors else None

    if title and first_author:
        titles_and_authors_alternative.append((title, first_author))

# Common English surnames for filtering
common_surnames = [
    "Aaliyah", "Aalyah", "Aaron", "Abdel", "Abdias", "Abdiel", "Abdielys", "Abdier", "Abdriel", "Abel", "Abiel", "Abiezer", "Abigail", "Abimael", "Abimelec", "Abisai", "Abnel", "Abner", "Abneris", "Abniel", "Abraham", "Ada", "Adahia", "Adaia", "Adaiah", "Adalberto", "Adalis", "Adaliz", "Adalys", "Adam", "Adamaris", "Adamarys", "Adams", "Adan", "Adara", "Addiel", "Addison", "Adela", "Adeline", "Adeliz", "Adelyn", "Adhara", "Adian", "Adianez", "Adiaris", "Adiel", "Adlin", "Adnel", "Adner", "Adniel", "Adolfo", "Adonis", "Adrialys", "Adriam", "Adrian", "Adriana", "Adrianis", "Adrianna", "Adrianys", "Adriel", "Adrielis", "Adrielys", "Adrien", "Adrik", "Adryan", "Adyan", "Agnes", "Agustin", "Ahinara", "Ahinoa", "Ahmed", "Aida", "Aidaliz", "Aidan", "Aiden", "Aihnara", "Aihnoa", "Ailana", "Ailani", "Ailanis", "Ailanna", "Ailany", "Ailanys", "Ailed", "Aileen", "Aimar", "Aimee", "Aina", "Ainara", "Ainarah", "Ainhara", "Ainhoa", "Ainoah", "Ainoha", "Airam", "Aisha", "Aitana", "Aithan", "Aixa", "Aj", "Ajani", "Akira", "Alahia", "Alahna", "Alaia", "Alaiah", "Alaiha", "Alaiia", "Alaila", "Alaina", "Alaixa", "Alaiya", "Alaiyah", "Alan", "Alana", "Alanah", "Alani", "Alanies", "Alanis", "Alaniz", "Alanna", "Alannah", "Alannis", "Alannys", "Alany", "Alanys", "Alaric", "Alaya", "Alayah", "Alayla", "Alayna", "Alaysha", "Alba", "Albert", "Alberto", "Aleah", "Aleanis", "Aleanys", "Alec", "Aleck", "Aleena", "Alegna", "Aleia", "Aleidy", "Aleira", "Aleisha", "Aleishka", "Alejandra", "Alejandro", "Alek", "Alena", "Alenis", "Aleris", "Aleshka", "Alessandra", "Alex", "Alexa", "Alexander", "Alexandra", "Alexandre", "Alexandria", "Alexavier", "Alexey", "Alexia", "Alexie", "Alexiel", "Alexis", "Alexsandra", "Alexxa", "Aleysha", "Aleyshka", "Alfonso", "Alfred", "Alfredo", "Alia", "Aliah", "Alian", "Aliana", "Alianis", "Alianna", "Aliannys", "Alianys", "Alice", "Alicia", "Alina", "Alisa", "Alisha", "Alison", "Alissa", "Aliyah", "Allan", "Allen", "Allison", "Allyson", "Alma", "Alondra", "Alonso", "Alvaro", "Alvin", "Alyah", "Alyanna", "Alysha", "Alyson", "Alyssa", "Amahia", "Amahya", "Amaia", "Amaiah", "Amaiia", "Amaiya", "Amalia", "Amanda", "Amani", "Amara", "Amari", "Amarilis", "Amarilys", "Amaris", "Amarys", "Amaury", "Amaya", "Amayah", "Amaziah", "Ambar", "Amber", "Amelia", "Amelie", "Amil", "Amilcar", "Amir", "Amira", "Amirah", "Amneris", "Amy", "Amylee", "Ana", "Anabel", "Anabella", "Anabelle", "Anaeli", "Anaelis", "Anahi", "Anahia", "Anahis", "Anaia", "Anaiah", "Anaid", "Anaili", "Anaily", "Anaira", "Anais", "Analia", "Anamaria", "Ananda", "Anastasia", "Anaya", "Ander", "Anderson", "Andre", "Andrea", "Andres", "Andrew", "Andrick", "Andriel", "Andy", "Aneily", "Aneisha", "Aneishka", "Anelis", "Anelisse", "Anelys", "Aneudi", "Aneudy", "Aneysha", "Aneyshka", "Anfernee", "Angel", "Angela", "Angelee", "Angeles", "Angeli", "Angelianys", "Angelic", "Angelica", "Angelie", "Angelik", "Angelika", "Angelimar", "Angelina", "Angeline", "Angelique", "Angelis", "Angelisse", "Angeliz", "Angelly", "Angelo", "Angely", "Angelys", "Angelyz", "Angie", "Anibal", "Aniel", "Anielis", "Anielys", "Anier", "Aniyah", "Ann", "Anna", "Annabelle", "Anne", "Anneliese", "Annelisse", "Annette", "Annie", "Anthonella", "Anthony", "Anthuan", "Antonella", "Antonio", "Antony", "Antuan", "Antwan", "Antwone", "Anya", "Anyelina", "Anyelis", "Aolani", "Aquiles", "Arabella", "Aracelis", "Aramis", "Aranis", "Aranza", "Arath", "Arelis", "Arelys", "Ares", "Argenis", "Aria", "Ariadna", "Ariadne", "Arialys", "Ariam", "Arian", "Ariana", "Arianis", "Arianna", "Arianne", "Ariannys", "Arianys", "Ariel", "Arielis", "Arieliz", "Ariella", "Arielys", "Arielyz", "Arizbeth", "Arleen", "Arlene", "Arlet", "Arleth", "Arlette", "Armando", "Armani", "Arnaldo", "Arnold", "Arthur", "Arturo", "Aruna", "Arwen", "Arya", "Aryam", "Aryana", "Aryanna", "Asael", "Ashanti", "Ashanty", "Asher", "Ashley", "Ashleyann", "Ashly", "Ashton", "Asia", "Asiel", "Aslan", "Aslin", "Astrid", "Atalia", "Athalia", "Athena", "Aubrey", "Augusto", "Aura", "Aurelio", "Aurelis", "Aurora", "Austin", "Ava", "Avery", "Axel",
    "Axiel", "Ayden", "Ayla", "Aymar", "Aynara", "Aysha", "Azael", "Azariel", "Azeneth", "Aziel", "Azul", "Bailey", "Baker", "Barbara", "Bastian", "Bayron", "Beatriz", "Bella", "Ben", "Benjamin", "Benny", "Berenice", "Bernardo", "Bernie", "Betsy", "Beverly", "Beyonce", "Bianca", "Bianka", "Billy", "Blanca", "Blessing", "Bowen", "Bradlee", "Bradley", "Braian", "Brandom", "Brandon", "Brandy", "Braulio", "Brayan", "Brayden", "Breanna", "Brenda", "Brendaliz", "Brian", "Briana", "Brianelys", "Brianna", "Brielle", "Brigitte", "Brihanna", "Britany", "Brithany", "Britney", "Brittany", "Brown", "Bruno", "Bryam", "Bryan", "Bryana", "Bryanna", "Bryant", "Bryce", "Byron", "Cairo", "Caitlin", "Caleb", "Calvin", "Camelia", "Cameron", "Camil", "Camila", "Camile", "Camilla", "Camille", "Camilo", "Campbell", "Carelis", "Careliz", "Carelys", "Caridad", "Carielys", "Carimar", "Carina", "Carl", "Carla", "Carlianis", "Carlianys", "Carlo", "Carlos", "Carmelo", "Carmen", "Carol", "Carola", "Carolina", "Caroline", "Carolyn", "Carolyne", "Carter", "Casey", "Cassandra", "Cataleia", "Cataleiah", "Cataleya", "Catalina", "Catherine", "Cattaleya", "Cattleya", "Cayden", "Cecilia", "Cedric", "Celeste", "Celimar", "Celines", "Celymar", "Cesar", "Chaliana", "Chanel", "Chantal", "Charity", "Charleen", "Charlene", "Charles", "Charlie", "Charlotte", "Charlyn", "Chelsea", "Chelsie", "Cheyenne", "Chloe", "Chris", "Chrislianys", "Christ", "Christal", "Christian", "Christiana", "Christie", "Christina", "Christine", "Christofer", "Christopher", "Ciara", "Cindy", "Claire", "Clara", "Claribel", "Clark", "Claudia", "Clayton", "Cloe", "Cody", "Cole", "Colin", "Collin", "Connor", "Coraima", "Coral", "Coralis", "Coraliz", "Coralys", "Cris", "Cristal", "Cristaly", "Cristhian", "Cristian", "Cristina", "Cristofer", "Cristopher", "Cristy", "Croitoru", "Cruz", "Crystal", "Cyd", "Cynthia", "Dael", "Daenerys", "Dahiana", "Dahianna", "Daiana", "Daila", "Daira", "Dairon", "Daisha", "Daisy", "Daleishka", "Dalia", "Daliana", "Dalianis", "Dalianys", "Dalimar", "Daliz", "Dalvin", "Dalymar", "Damaris", "Damian", "Damien", "Dan", "Dana", "Dandre", "Daneisha", "Daneishalys", "Daneishka", "Danel", "Danelis", "Danelys", "Daneysha", "Daneyshka", "Dangelo", "Dania", "Daniel", "Daniela", "Danielis", "Danieliz", "Daniella", "Danielle", "Danielys", "Danielyz", "Danisha", "Danishka", "Danna", "Danny", "Dante", "Danyael", "Daphne", "Dara", "Darel", "Darelis", "Darell", "Darelys", "Daren", "Darian", "Dariana", "Darianis", "Darianna", "Darianne", "Darianys", "Dariel", "Darielis", "Darieliz", "Darielys", "Darien", "Dario", "Darius", "Darkiel", "Darleen", "Darlene", "Darlyn", "Darren", "Darwin", "Dashira", "Davian", "Daviana", "David", "Daviel", "Davielys", "Davier", "Davis", "Daxiel", "Dayan", "Dayana", "Dayanara", "Dayane", "Dayaneira", "Dayanis", "Dayanna", "Dayanne", "Dayna", "Daynelis", "Dayra", "Dayron", "Dean", "Deandre", "Debbie", "Debora", "Deborah", "Delaney", "Delia", "Delianys", "Delilah", "Delimar", "Delmarie", "Delmaris", "Delmarys", "Delvin", "Delvis", "Delwin", "Demian", "Deniel", "Denielys", "Denis", "Denise", "Denisse", "Dennis", "Denny", "Dennys", "Denzel", "Dereck", "Derek", "Deric", "Derick", "Deriel", "Derik", "Derrick", "Derwin", "Desire", "Desiree", "Destiny", "Devin", "Devon", "Devonte", "Dexter", "Deyaneira", "Deylianis", "Dian", "Diana", "Dianaliz", "Diane", "Dianelis", "Dianeliz", "Dianelys", "Dianelyz", "Diego", "Dilan", "Dimas", "Dimosthenis", "Dinoshka", "Diomar", "Dionel", "Doel", "Dolly", "Domingo", "Dominic", "Dominique", "Donovan", "Dorian", "Doriann", "Dorimar", "Doris", "Doruk", "Douglas", "Drake", "Dulce", "Duvan", "Dwayne", "Dwight", "Dylan", "Dyland", "Dylann", "Dylara", "Eason", "Ebdiel", "Ed", "Eddie", "Eddiel", "Eddy", "Ederick", "Edgar", "Edgard", "Edgardo", "Edian", "Edianys", "Ediel", "Edielys", "Edil", "Edison", "Edith", "Edmarie", "Edna", "Edniel", "Edrian", "Edric", "Edrick", "Edriel", "Edrik", "Edsel", "Eduard", "Eduardo", "Edward", "Edwin", "Edziel", "Efrain", "Efren", "Eidan", "Eiden", "Eider", "Eileen", "Eilianys", "Eimy", "Eiram", "Eitan", "Eithan", "Ektor", "Elaine", "Elba", "Eleazar", "Elena", "Eli", "Eliab", "Eliam",
    "Elian", "Eliana", "Elianis", "Elianna", "Eliany", "Elianys", "Elias", "Eliel", "Elienai", "Elier", "Eliette", "Eliezer", "Elif", "Elijah", "Elimar", "Elimelec", "Eliomar", "Elionaid", "Eliot", "Elis", "Elisa", "Elisamuel", "Eliseo", "Elisha", "Eliud", "Eliz", "Eliza", "Elizabeth", "Elizbeth", "Elizmarie", "Ella", "Elliot", "Elliott", "Ellis", "Elmer", "Eloise", "Eloy", "Elsa", "Elsie", "Elvin", "Elvis", "Ema", "Emanuel", "Emanuelle", "Emely", "Emil", "Emilia", "Emiliana", "Emiliano", "Emilianys", "Emilie", "Emilio", "Emilly", "Emily", "Emir", "Emma", "Emmanuel", "Emmanuelle", "Endel", "Engel", "Enid", "Eniel", "Enoc", "Enrico", "Enrique", "Enya", "Enyel", "Enzo", "Eren", "Erian", "Erianys", "Eric", "Erica", "Erick", "Ericka", "Erickson", "Ericson", "Eriel", "Erielys", "Erik", "Erika", "Erin", "Ernesto", "Ernie", "Ervin", "Erwin", "Esai", "Esmeralda", "Esteban", "Estefani", "Estefania", "Estefanie", "Estefany", "Estela", "Estephanie", "Ester", "Esthefany", "Esther", "Estrella", "Ethan", "Etienne", "Eugene", "Eugenio", "Eunice", "Eva", "Evaluna", "Evan", "Evangeline", "Evangely", "Evans", "Evelyn", "Evolet", "Eydan", "Eyden", "Eythan", "Ezekiel", "Ezequiel", "Ezra", "Fabbri", "Fabian", "Fabiana", "Fabio", "Fabiola", "Faith", "Farah", "Fatima", "Favian", "Faviana", "Faviola", "Federico", "Felipe", "Felisha", "Felix", "Ferdinand", "Fernan", "Fernanda", "Fernando", "Fiona", "Flor", "Florence", "Flores", "Francelys", "Frances", "Francheliz", "Franchely", "Franchelys", "Franchesca", "Francheska", "Francis", "Francisco", "Franco", "Frank", "Frankie", "Franklin", "Franklyn", "Fransheska", "Freddie", "Freddy", "Frederick", "Gabriel", "Gabriela", "Gabrielis", "Gabrieliz", "Gabriella", "Gabrielle", "Gabrielys", "Gaddiel", "Gadiel", "Gadriel", "Gael", "Gaia", "Galilea", "Gamaliel", "Gamalier", "Garcia", "Gary", "Gavin", "Gean", "Gema", "Gemma", "Genesis", "Genessis", "George", "Georges", "Geovanni", "Geovanny", "Geral", "Gerald", "Geraldine", "Geraldo", "Geralys", "Gerard", "Gerardo", "Geremy", "Geriel", "German", "Gerson", "Gia", "Giah", "Giam", "Gian", "Giana", "Giancarlo", "Giancarlos", "Gianella", "Gianelys", "Gianluca", "Gianmarco", "Giann", "Gianna", "Gibran", "Gil", "Gilbert", "Gilberto", "Gilianys", "Gilmarie", "Gina", "Ginelys", "Gino", "Gio", "Giomar", "Giovan", "Giovani", "Giovaniel", "Giovanna", "Giovanni", "Giovannie", "Giovanniel", "Giovanny", "Giovany", "Gisela", "Giselle", "Gisselle", "Giuliana", "Giuliano", "Gladymar", "Gladys", "Glenda", "Glenn", "Glerisbeth", "Glerys", "Glerysbet", "Glerysbeth", "Gloria", "Glorialys", "Glorian", "Glorianis", "Gloriann", "Glorianne", "Glorianys", "Glorielys", "Glorimar", "Glory", "Glorymar", "Gonzalez", "Gonzalo", "Grace", "Graciela", "Grayson", "Grecia", "Green", "Gregory", "Greidys", "Greisha", "Gretchen", "Greysha", "Griselle", "Guarionex", "Guillermo", "Gustavo", "Hailey", "Hakeem", "Haley", "Hall", "Hamilton", "Haniel", "Hanna", "Hannah", "Hansel", "Hanzel", "Harold", "Harris", "Harry", "Haydee", "Hayden", "Haylee", "Hazael", "Hazel", "Haziel", "Hecdiel", "Hecmarie", "Hecniel", "Hector", "Heidi", "Heidy", "Heily", "Helen", "Helena", "Henrry", "Henry", "Heriberto", "Herman", "Hermione", "Hernan", "Hernandez", "Hilary", "Hilda", "Hill", "Hillary", "Hiram", "Hommy", "Hope", "Hugo", "Humberto", "Hunter", "Iam", "Ian", "Iann", "Ibrahim", "Idalis", "Idaliz", "Idalys", "Ignacio", "Ihan", "Iker", "Ilai", "Ilan", "Ilana", "Ilanit", "Ileana", "Iliana", "Ilianis", "Iliany", "Ilianys", "Imalay", "Imanol", "Inara", "Indira", "Ines", "Ingrid", "Irelis", "Irene", "Irianis", "Irianys", "Iris", "Irmarie", "Irvin", "Irving", "Irwin", "Isaac", "Isabel", "Isabela", "Isabella", "Isabelle", "Isac", "Isadora", "Isael", "Isai", "Isaiah", "Isaias", "Isamar", "Isamarie", "Isamary", "Isander", "Isis", "Isla", "Ismael", "Ismarie", "Israel", "Ithan", "Itzael", "Itzamar", "Itzan", "Itzayana", "Itzel", "Ivan", "Ivana", "Ivanelis", "Ivaneliz", "Ivanelys", "Ivaniel", "Ivanis", "Ivanna", "Ivelisse", "Iverson", "Ivette", "Ivonne", "Ixander", "Izabella", "Izaiah", "Izan", "Jaasiel", "Jaaziel", "Jabdiel", "Jabes", "Jabneel", "Jabnel", "Jace", "Jaciel", "Jack",
    "Jackdiel", "Jackeline", "Jackniel", "Jackson", "Jackxiel", "Jacob", "Jacqueline", "Jada", "Jaddiel", "Jade", "Jadel", "Jaden", "Jadiel", "Jadielis", "Jadielys", "Jadier", "Jadniel", "Jadrian", "Jadriel", "Jael", "Jaelis", "Jaelys", "Jafed", "Jafet", "Jahaziel", "Jahdiel", "Jahel", "Jahir", "Jahn", "Jahzeel", "Jahziel", "Jaicob", "Jaiden", "Jaileen", "Jailene", "Jaime", "Jair", "Jairo", "Jake", "Jalianys", "Jalil", "Jam", "Jamal", "Jamaris", "James", "Jamian", "Jamie", "Jamil", "Jamilette", "Jan", "Jancarlo", "Jancarlos", "Janciel", "Jandaniel", "Jandel", "Jandiel", "Jandre", "Jandriel", "Jane", "Janeidy", "Janeilys", "Janeirys", "Janeishka", "Janelis", "Janelisse", "Janeliz", "Janelle", "Janelly", "Janellys", "Janely", "Janelys", "Janerys", "Janet", "Janette", "Janeyshka", "Jangel", "Janice", "Janiel", "Janielis", "Janieliz", "Janielys", "Janier", "Janiliz", "Janina", "Janisha", "Janishka", "Janitza", "Jankiel", "Janlean", "Janlee", "Janluis", "Jann", "Janniel", "Janpaul", "Jansel", "Jansiel", "Januel", "Janvier", "Janxel", "Janxiel", "Janziel", "Japhet", "Jared", "Jarel", "Jarelis", "Jareliz", "Jarell", "Jarelys", "Jareth", "Jariana", "Jariel", "Jarielis", "Jarieliz", "Jarielys", "Jashira", "Jashua", "Jasiel", "Jaslene", "Jasmin", "Jasmine", "Jason", "Jasper", "Jassiel", "Jathniel", "Jatniel", "Jatziel", "Javian", "Javiel", "Javielis", "Javieliz", "Javielys", "Javier", "Jaxiel", "Jaxier", "Jay", "Jayce", "Jayco", "Jaycob", "Jayda", "Jaydaliz", "Jaydan", "Jaydeen", "Jaydeliz", "Jaydem", "Jayden", "Jaydiel", "Jaydrian", "Jaydriel", "Jayko", "Jaykob", "Jayla", "Jaylah", "Jayleen", "Jaylen", "Jaylianis", "Jayliz", "Jaymar", "Jaymarie", "Jayniel", "Jayren", "Jayriel", "Jayro", "Jayron", "Jayson", "Jaythan", "Jayven", "Jayvier", "Jayvin", "Jazer", "Jaziel", "Jazmin", "Jazmine", "Jean", "Jeancarlos", "Jeandiel", "Jeandriel", "Jeaneliz", "Jeanelys", "Jeanette", "Jeannette", "Jeanpaul", "Jediael", "Jediel", "Jedrian", "Jedrick", "Jedriel", "Jedziel", "Jefferson", "Jeffrey", "Jeffry", "Jefrey", "Jefte", "Jehiel", "Jehieli", "Jeicob", "Jeiden", "Jeidy", "Jeika", "Jeilianis", "Jeilianys", "Jeimy", "Jeiren", "Jelianis", "Jeliannys", "Jelianys", "Jeliel", "Jemuel", "Jen", "Jenaiah", "Jenay", "Jencarlos", "Jendiel", "Jendriel", "Jeniel", "Jenielis", "Jeniell", "Jenielys", "Jenier", "Jenifer", "Jeniffer", "Jenilca", "Jenilka", "Jenitza", "Jenna", "Jenniel", "Jennielys", "Jennifer", "Jenniffer", "Jenny", "Jensel", "Jensen", "Jensiel", "Jenuel", "Jenxiel", "Jenzel", "Jenziel", "Jerald", "Jeralys", "Jeray", "Jereck", "Jerek", "Jerel", "Jeremi", "Jeremiah", "Jeremias", "Jeremie", "Jeremmy", "Jeremy", "Jerialys", "Jerianys", "Jericho", "Jerick", "Jeriel", "Jerielys", "Jerika", "Jermaine", "Jerome", "Jeromy", "Jeroy", "Jerry", "Jersen", "Jeryel", "Jesenia", "Jeshua", "Jesiah", "Jesiel", "Jeslian", "Jesliany", "Jeslianys", "Jesmarie", "Jesmary", "Jesse", "Jessenia", "Jessica", "Jessie", "Jessiel", "Jessmarie", "Jesuan", "Jesuel", "Jesus", "Jethziel", "Jetniel", "Jetsiel", "Jetxiel", "Jetzel", "Jetziel", "Jetzuel", "Jexiel", "Jeycob", "Jeydan", "Jeydem", "Jeyden", "Jeydiel", "Jeydrian", "Jeydriel", "Jeylian", "Jeylianis", "Jeylimar", "Jeymarie", "Jeyniel", "Jeyren", "Jeyrianis", "Jeyriel", "Jeysen", "Jeysha", "Jeyvier", "Jeziel", "Jezreel", "Jhan", "Jhensen", "Jhomar", "Jhon", "Jhoniel", "Jian", "Jianna", "Jim", "Jimena", "Jimmy", "Jinelys", "Jireh", "Joadiel", "Joalis", "Joalys", "Joan", "Joandriel", "Joanel", "Joanelis", "Joaneliz", "Joanelys", "Joaniel", "Joanielys", "Joanmarie", "Joann", "Joanna", "Joanne", "Joanys", "Joaquin", "Joarelys", "Joaris", "Jocelyn", "Jocelyne", "Jocsan", "Jodiel", "Joe", "Joel", "Joelianis", "Joelianys", "Joeliel", "Joelis", "Joeliz", "Joely", "Joelys", "Joelyz", "Joemar", "Joeniel", "Joeseph", "Joey", "Johalis", "Johalys", "Johan", "Johana", "Johanelis", "Johaneliz", "Johanelys", "Johaniel", "Johann", "Johanna", "Johanne", "Johanny", "Joharis", "Joharys", "John", "Johnathan", "Johndiel", "Johndriel", "Johnel", "Johniel", "Johnniel", "Johnny", "Johnpaul", "Johnsiel", "Johnson", "Johnuel", "Jolianys", "Jolimar", "Jomal", "Jomar", "Jomarie", "Jomarielys", "Jomaris", "Jomary", "Jomarys", "Jomayra", "Jometh", "Jon", "Jonael", "Jonah", "Jonairys", "Jonaliz", "Jonalys",
    "Jonas", "Jonatan", "Jonathan", "Jonay", "Jondriel", "Joneilys", "Jonel", "Jonell", "Jonelys", "Jones", "Joniel", "Jonielys", "Jonier", "Jonnathan", "Jonniel", "Jonuel", "Jordan", "Jordany", "Jordiel", "Jordy", "Jorel", "Jorelis", "Jorell", "Jorelys", "Jorge", "Joriel", "Jorielys", "Jorlianys", "Josdiel", "Jose", "Josean", "Joseline", "Joselyn", "Joselyne", "Joseph", "Josephine", "Josh", "Joshniel", "Joshua", "Joshuan", "Joshuel", "Josiah", "Josian", "Josias", "Josiel", "Josielys", "Josimar", "Josliany", "Joslianys", "Josmarie", "Josmary", "Josniel", "Jossie", "Josten", "Jostin", "Jostyn", "Josuan", "Josue", "Josuel", "Jouseph", "Jovan", "Jovaniel", "Jovanka", "Jovanny", "Jovany", "Jovian", "Jowel", "Jowell", "Jowen", "Joxiel", "Joy", "Joyce", "Joycemarie", "Jr", "Juan", "Jude", "Judith", "Judy", "Juleisy", "Julia", "Julian", "Juliana", "Julianette", "Julianie", "Julianis", "Julianna", "Julianne", "Juliannie", "Juliannys", "Juliany", "Julianys", "Julie", "Julieann", "Juliemar", "Juliet", "Julieta", "Juliette", "Julimar", "Julio", "Julisa", "Julissa", "Julitza", "Juliza", "Julymar", "June", "Juniel", "Junielys", "Junior", "Juriel", "Justin", "Justine", "Justo", "Justyn", "Kaden", "Kadiel", "Kaeden", "Kael", "Kaelys", "Kahil", "Kai", "Kaiden", "Kailani", "Kailany", "Kailanys", "Kaira", "Kairi", "Kairo", "Kaitlyn", "Kaleb", "Kaled", "Kalel", "Kaleth", "Kaleysha", "Kalia", "Kalianys", "Kaliel", "Kalil", "Kamelia", "Kamil", "Kamila", "Kamilah", "Kamilia", "Kamilla", "Kamille", "Kamilo", "Kamyla", "Kaniel", "Kareem", "Karelis", "Karelisse", "Kareliz", "Karelyn", "Karelys", "Karen", "Kariam", "Karian", "Kariana", "Kariangelys", "Karianis", "Karianys", "Kariel", "Karielis", "Karielys", "Karielyz", "Karilys", "Karim", "Karimar", "Karimi", "Karina", "Karines", "Karl", "Karla", "Karlianys", "Karlo", "Karlos", "Karol", "Karola", "Karolina", "Karoline", "Karolyn", "Karolyna", "Karolyne", "Karymar", "Kasandra", "Kasey", "Kassandra", "Kataleia", "Kataleiah", "Kataleya", "Katalina", "Kate", "Katelyn", "Katerina", "Kathaleia", "Kathaleya", "Kathalina", "Katherine", "Kathia", "Kathiana", "Kathiria", "Kathleen", "Kathy", "Kathyana", "Kathyria", "Katia", "Katiana", "Katiria", "Katiushka", "Katiuska", "Katrina", "Kattaleia", "Kaya", "Kayden", "Kayla", "Kaylanis", "Kaylee", "Kayra", "Keanu", "Kediel", "Kedniel", "Kedrian", "Kedrick", "Kedriel", "Kedwin", "Kefren", "Kehlani", "Keiden", "Keidy", "Keila", "Keilany", "Keilanys", "Keiliany", "Keilianys", "Keily", "Keilyn", "Keira", "Keisha", "Keishaly", "Keishla", "Keishlian", "Keishliany", "Keishlianys", "Keishly", "Keishlyann", "Keisy", "Keith", "Kekoa", "Kelaia", "Kelianis", "Keliany", "Kelianys", "Keliel", "Kelly", "Kellyanis", "Kellyann", "Kellymar", "Kelvin", "Kelwin", "Kemuel", "Kenai", "Kenan", "Kenay", "Kendall", "Kendra", "Kendric", "Kendrick", "Kendriel", "Kendryel", "Keneth", "Kenia", "Kenialys", "Keniel", "Keniell", "Kenielle", "Kenielys", "Kenisha", "Kennay", "Kennet", "Kenneth", "Kennette", "Kenniel", "Kenny", "Kennyel", "Kenuel", "Kenxiel", "Kenya", "Kenyel", "Kenziel", "Keoni", "Keren", "Kerialys", "Kerianys", "Keriel", "Kerielys", "Kerim", "Kermit", "Kervin", "Keshawn", "Ketxiel", "Ketziel", "Keven", "Kevian", "Kevianys", "Keviel", "Kevin", "Kevyn", "Keycha", "Keydan", "Keyden", "Keyla", "Keylanie", "Keylian", "Keylianie", "Keylianis", "Keylianiz", "Keyliann", "Keylianys", "Keylimar", "Keymarie", "Keyra", "Keysha", "Keyshaliz", "Keyshla", "Keyshlian", "Keythan", "Khaleb", "Khaled", "Khaleesi", "Khalid", "Khalil", "Khamila", "Kharla", "Khloe", "Khris", "Khriz", "Kiam", "Kian", "Kiana", "Kianelys", "Kianna", "Kiany", "Kiara", "Kiaralis", "Kiaraliz", "Kiaralys", "Kiarelis", "Kiareliz", "Kiarelys", "Kidanny", "Kidany", "Kiliam", "Kilian", "Killian", "Kim", "Kimberlie", "Kimberly", "Kinaisha", "Kinaysha", "Kineisha", "Kineysha", "King", "Kiomara", "Kira", "Kiria", "Kirialys", "Kisha", "Kjani", "Kobe", "Koralis", "Koralys", "Kris", "Kristal", "Kristen", "Kristhian", "Kristian", "Kristina", "Kristopher", "Kristy", "Krizia", "Krystal", "Krystel", "Krystian", "Kyan", "Kyara", "Kyla", "Kyle", "Kylian", "Kylie", "Kymani", "Kynaisha", "Kyra", "Lady", "Lahia", "Laia", "Laiah", "Laila", "Laisa", "Laisha", "Laiza", "Laleshka",
    "Laleyshka", "Lance", "Landon", "Landy", "Lara", "Larah", "Larimar", "Larissa", "Larry", "Laura", "Lauren", "Laurie", "Lawrence", "Layla", "Layra", "Laysha", "Layza", "Lea", "Leah", "Leamsi", "Leandra", "Leandro", "Leann", "Lee", "Leeann", "Legna", "Leia", "Leiah", "Leila", "Leilani", "Leilanie", "Leilanis", "Leilany", "Leilanys", "Leilianys", "Leira", "Leire", "Leisha", "Leishka", "Leland", "Lemuel", "Leniel", "Lenniel", "Lenny", "Leo", "Leomar", "Leon", "Leonard", "Leonardo", "Leonel", "Leonela", "Leonelys", "Leriel", "Leroy", "Leslian", "Leslie", "Lesly", "Lester", "Levi", "Lewis", "Lexian", "Lexiel", "Leyka", "Leyla", "Leyra", "Leysha", "Leyshka", "Leyshla", "Lia", "Liah", "Liam", "Lian", "Liana", "Lianelys", "Lianette", "Lianis", "Liann", "Lianna", "Lianny", "Liannys", "Liany", "Lianys", "Liara", "Liliana", "Lilianys", "Lilliam", "Lillian", "Lilliana", "Lily", "Lina", "Lincoln", "Linda", "Lindsey", "Lineishka", "Linette", "Lineyshka", "Linnette", "Linoshka", "Lionel", "Lis", "Lisa", "Lisandra", "Lisandro", "Lisbet", "Lisbeth", "Lismar", "Lismarie", "Lismary", "Lissette", "Livan", "Liz", "Liza", "Lizandra", "Lizbeth", "Lizmar", "Lizmarie", "Lizmary", "Logan", "Lopez", "Loraine", "Loren", "Lorena", "Lorenzo", "Lorianne", "Lorna", "Lorraine", "Louis", "Lourdes", "Loyda", "Lua", "Luan", "Luca", "Lucas", "Lucca", "Luccas", "Lucero", "Lucia", "Luciana", "Luciano", "Lucy", "Luian", "Luis", "Luisa", "Luisangel", "Luka", "Lukas", "Luke", "Luna", "Lunna", "Luz", "Luzmarie", "Lya", "Lyah", "Lyam", "Lyan", "Lyanis", "Lyann", "Lyanna", "Lyanne", "Lyannette", "Lyannis", "Lydia", "Lymarie", "Lynette", "Lynnette", "Lynoshka", "Madeline", "Madison", "Magdiel", "Magerly", "Mahia", "Maia", "Maicol", "Maila", "Mairim", "Maite", "Makayla", "Malachi", "Malakai", "Malcom", "Malena", "Malia", "Malik", "Malvin", "Manolis", "Manuel", "Mara", "Marangeli", "Marangelie", "Marangelis", "Marangeliz", "Marangely", "Marangelys", "Marc", "Marcel", "Marcela", "Marcelo", "Marco", "Marcos", "Marcus", "Marelys", "Marena", "Margaret", "Margarita", "Mari", "Maria", "Mariah", "Marialejandra", "Marializ", "Marialys", "Marialyz", "Mariam", "Marian", "Mariana", "Mariangel", "Mariangela", "Mariangeli", "Mariangelie", "Mariangelis", "Mariangeliz", "Mariangely", "Mariangelys", "Marianna", "Marianne", "Mariano", "Maribel", "Maricarmen", "Maricelis", "Maricelys", "Marie", "Mariel", "Mariela", "Marielena", "Marielis", "Marielisa", "Marieliz", "Mariely", "Marielys", "Mariliana", "Mariliz", "Marilyn", "Marimar", "Marina", "Mario", "Mariola", "Marisabel", "Marisol", "Marissa", "Maritza", "Marjorie", "Mark", "Markus", "Marla", "Marlene", "Marley", "Marlon", "Marlyn", "Marta", "Martha", "Martin", "Martinez", "Marvin", "Mary", "Maryann", "Marymar", "Maryorie", "Mason", "Massimo", "Mateo", "Matheo", "Mathew", "Mathias", "Matias", "Matteo", "Matthew", "Matthias", "Mattias", "Mauricio", "Mauro", "Max", "Maximiliano", "Maximo", "Maxwell", "Maxximo", "Maya", "Maycol", "Mayerli", "Mayerlie", "Mayerly", "Mayra", "Mayrelis", "Megan", "Meghan", "Melani", "Melanie", "Melannie", "Melanny", "Melany", "Mele", "Melianis", "Melianys", "Melissa", "Melody", "Melquisedec", "Melton", "Melvin", "Melwin", "Meralys", "Mercedes", "Meredith", "Mia", "Miah", "Micael", "Micaela", "Micah", "Michael", "Michell", "Michelle", "Mickaela", "Migdalia", "Migdaliz", "Miguel", "Miguelangel", "Mikael", "Mikaela", "Mikaelah", "Mikaele", "Mikaella", "Mikahela", "Mikayla", "Mike", "Mikeila", "Mikel", "Mikeyla", "Mikhail", "Mila", "Milady", "Milagros", "Milah", "Milan", "Milca", "Mileidy", "Mileishka", "Milena", "Milenna", "Miley", "Mileyka", "Mileysha", "Mileyshka", "Miliany", "Milianys", "Militza", "Miller", "Milo", "Milton", "Minelys", "Minerva", "Minoshka", "Miosotis", "Miracle", "Miran", "Miranda", "Miredys", "Mirelis", "Mireliz", "Mirelys", "Mireya", "Miriam", "Mirielys", "Misael", "Mitchell", "Mizael", "Mj", "Moesha", "Moises", "Monica", "Monika", "Moore", "Moraima", "Moses", "Mya", "Myah", "Mykaela", "Mylena", "Myrelis", "Naara", "Nachali", "Nachalie", "Nachaly", "Nadeisha", "Nadesha", "Nadeshka", "Nadeysha", "Nadia", "Nadja", "Nadya", "Nadyalee", "Nael", "Naelys", "Nagely",
    "Nagelys", "Nahara", "Nahel", "Nahia", "Nahiara", "Nahiely", "Nahielys", "Nahiomy", "Nahir", "Nahomi", "Nahomy", "Naia", "Naiah", "Naiara", "Naidelyn", "Naiely", "Naielys", "Naihara", "Naihomy", "Naila", "Nailah", "Nailyn", "Naiomi", "Naiomy", "Nairobi", "Naisha", "Naishalee", "Naishaly", "Naishka", "Naiyelis", "Nakisha", "Naleishka", "Nallely", "Nancy", "Nanishka", "Naomi", "Naomy", "Nashalee", "Nashali", "Nashalie", "Nashaliz", "Nashally", "Nashaly", "Nashalys", "Nashira", "Nashly", "Natacha", "Natali", "Natalia", "Natalie", "Nataly", "Natanael", "Nataniel", "Natasha", "Nathalia", "Nathalie", "Nathaly", "Nathan", "Nathanael", "Nathaniel", "Nathasha", "Natisha", "Natshalie", "Natshaly", "Nayara", "Naydeline", "Naydeliz", "Nayelee", "Nayeli", "Nayelie", "Nayelis", "Nayeliz", "Nayelli", "Nayellie", "Nayelly", "Nayely", "Nayelys", "Nayhara", "Nayla", "Naylah", "Nayomi", "Naysha", "Nayshka", "Naythan", "Nayzeth", "Neftali", "Nehemias", "Neisha", "Neishalee", "Neishalie", "Neishaliz", "Neishaly", "Neishalys", "Neishka", "Neithan", "Neizan", "Nelianys", "Nellyann", "Nelmarie", "Nelson", "Nelvin", "Nemesis", "Nerielys", "Nestor", "Nevaeh", "Neycha", "Neyden", "Neymar", "Neysha", "Neyshalee", "Neyshalie", "Neyshka", "Neyshmarie", "Neythan", "Nguyen", "Nia", "Niccolo", "Nicholas", "Nichole", "Nick", "Nickolas", "Nico", "Nicohl", "Nicol", "Nicolas", "Nicole", "Nicolle", "Nikauly", "Nikolas", "Nilda", "Nileyshka", "Nilka", "Nilmarie", "Nina", "Ninoshka", "Ninoska", "Niurka", "Noa", "Noah", "Noe", "Noel", "Noelia", "Noelis", "Noeliz", "Noelys", "Noemi", "Nohely", "Nolan", "Nomar", "Nomaris", "Nomarys", "Noralis", "Norbert", "Norberto", "Norelis", "Norelys", "Noriel", "Norielis", "Norielys", "Norkis", "Norkys", "Norma", "Norman", "Normarie", "Normaris", "Normarys", "Nova", "Nyah", "Nydia", "Obed", "Ocean", "Odalis", "Odaliz", "Odalys", "Odlanier", "Olga", "Oliver", "Olivia", "Olvin", "Omaet", "Omar", "Omarielys", "Omaris", "Omarys", "Omayra", "Oneill", "Oniel", "Onix", "Onyx", "Oriana", "Orion", "Orlando", "Orlianys", "Oscar", "Oseias", "Osiris", "Osmar", "Osvaldo", "Oswaldo", "Owen", "Ozan", "Pablo", "Pahola", "Paloma", "Pamela", "Paola", "Paolo", "Patria", "Patricia", "Patrick", "Paul", "Paula", "Paulette", "Paulina", "Paulo", "Paz", "Pedro", "Penelope", "Perez", "Perla", "Peter", "Philip", "Phillip", "Pia", "Pilar", "Pj", "Precious", "Preston", "Prince", "Princesa", "Princess", "Priscila", "Priscilla", "Prune", "Rachel", "Rachell", "Rachelle", "Radames", "Rafael", "Raina", "Raisa", "Raiza", "Ralph", "Ramirez", "Ramiro", "Ramon", "Ramses", "Randall", "Randiel", "Randy", "Raquel", "Rashel", "Raul", "Ray", "Rayan", "Rayden", "Raymond", "Rayniel", "Raysa", "Raziel", "Rebeca", "Rebecca", "Reggie", "Reina", "Reinaldo", "Renata", "Rene", "Reniel", "Rey", "Reymond", "Reynaldo", "Reyniel", "Ricardo", "Richard", "Ricky", "Rico", "Rihanna", "Riley", "Rivera", "Robert", "Roberto", "Roberts", "Robinson", "Rochelle", "Rocio", "Roderick", "Rodney", "Rodniel", "Rodolfo", "Rodrigo", "Rodriguez", "Roger", "Roland", "Rolando", "Roman", "Romeo", "Ronald", "Ronaldo", "Roniel", "Ronnie", "Ronny", "Rosa", "Rosalinda", "Rosalyn", "Rosangela", "Rosangely", "Rosaura", "Rose", "Roselyn", "Rosemarie", "Rosemary", "Roxana", "Roy", "Ruben", "Rubi", "Rubielys", "Ruby", "Rut", "Ruth", "Ryan", "Ryann", "Ryder", "Sabdiel", "Sabrina", "Sachenka", "Sadie", "Sael", "Sahara", "Sahid", "Sahil", "Sahily", "Sahir", "Sahira", "Said", "Sailh", "Salome", "Salvador", "Salvation", "Sam", "Samantha", "Samara", "Samaris", "Samary", "Samil", "Samir", "Samira", "Samirah", "Sammy", "Samuel", "Sanchez", "Sandra", "Saned", "Santiago", "Santos", "Sara", "Sarah", "Sarahi", "Sarai", "Sarielys", "Saritza", "Sasha", "Saul", "Savannah", "Scarlett", "Scott", "Sean", "Sebasthian", "Sebastian", "Selena", "Serenity", "Sergio", "Seth", "Shaddai", "Shadiel", "Shaila", "Shailyn", "Shaina", "Shaira", "Shakira", "Shalim", "Shalimar", "Shalymar", "Shane", "Shanelys", "Shania", "Shanielys", "Shanik", "Shanira", "Shantal", "Shaquille", "Sharelys", "Sharielys", "Sharimar", "Sharleen", "Sharlene", "Sharlyn", "Sharon", "Shastelyn", "Shawn", "Shayna",
    "Shayra", "Sheila", "Sheiliany", "Sheilianys", "Sheily", "Shelimar", "Sherley", "Sherlian", "Sherly", "Sherlyn", "Sheyla", "Shirley", "Siaosi", "Siara", "Sidharth", "Sierra", "Sigfredo", "Silvia", "Simon", "Singh", "Sione", "Siul", "Sixto", "Sky", "Skyler", "Smith", "Sofia", "Sol", "Solange", "Soleil", "Solianys", "Solimar", "Solmarie", "Solymar", "Sonia", "Sonny", "Sonya", "Sophia", "Sophie", "Soraya", "Stacey", "Stacy", "Stefanie", "Stella", "Stephanie", "Stephany", "Stephen", "Steve", "Steven", "Sudhakaran", "Sugeily", "Suheily", "Sujeily", "Suleika", "Suleimy", "Suleyka", "Summer", "Sunel", "Surielys", "Sydney", "Sylvia", "Tabatha", "Taina", "Tais", "Taisha", "Taishaly", "Talisha", "Tamar", "Tamara", "Tanairi", "Tanairis", "Tanairy", "Taneisha", "Tania", "Tanisha", "Tanishka", "Tanya", "Tanysha", "Tara", "Tariq", "Tashira", "Tatiana", "Tatyana", "Tavita", "Taylor", "Tayra", "Taysha", "Teo", "Teresa", "Terrell", "Thaily", "Thais", "Thaisha", "Thalia", "Thanairy", "Thania", "Theo", "Theodore", "Theresa", "Thiago", "Thian", "Thomas", "Thompson", "Thyago", "Tia", "Tiago", "Tiana", "Tiara", "Tiffany", "Timothy", "Tina", "Tisha", "Tj", "Tobias", "Tomas", "Tommy", "Tony", "Torres", "Travis", "Trevor", "Trinity", "Tristan", "Troy", "Tyler", "Tyra", "Tyron", "Tyrone", "Ulises", "Urayoan", "Uriel", "Uziel", "Uzziel", "Valentina", "Valentino", "Valeria", "Valerie", "Valery", "Vanelys", "Vanessa", "Venus", "Veronica", "Veronika", "Verushka", "Vianca", "Vianka", "Vicent", "Vicente", "Vicmarie", "Victor", "Victoria", "Vida", "Vilmarie", "Vilmary", "Vincent", "Violet", "Violeta", "Virgen", "Virginia", "Vivian", "Viviana", "Vladimir", "Waldemar", "Waldo", "Waleska", "Walker", "Walter", "Wanda", "Wayne", "Wendell", "Wendy", "Wesley", "Weslie", "Wesly", "White", "Widalys", "Wil", "Wilbert", "Wilberto", "Wildaliz", "Wildalys", "Wileyshka", "Wilfred", "Wilfredo", "Wilkins", "Will", "William", "Williams", "Willianys", "Willie", "Wilmari", "Wilmarie", "Wilmaris", "Wilmary", "Wilmarys", "Wilmer", "Wilnelis", "Wilnelys", "Wilson", "Wright", "Wyatt", "Xabdiel", "Xadiel", "Xael", "Xamir", "Xander", "Xarielys", "Xaviel", "Xavielys", "Xavier", "Xaymara", "Xaymarie", "Xian", "Xiara", "Ximena", "Xiomara", "Xiomarie", "Xionelys", "Yabdiel", "Yabdriel", "Yabriel", "Yachira", "Yacxiel", "Yaddeliz", "Yaddiel", "Yadelis", "Yadeliz", "Yadhiel", "Yadiel", "Yadielis", "Yadieliz", "Yadielys", "Yadier", "Yadimar", "Yadira", "Yadniel", "Yadrian", "Yadriana", "Yadriel", "Yadrielis", "Yadrieliz", "Yadrielys", "Yadxiel", "Yael", "Yaelis", "Yaeliz", "Yahaira", "Yahdiel", "Yahel", "Yahil", "Yahir", "Yahve", "Yahveh", "Yaidelice", "Yaidelis", "Yaideliz", "Yaiden", "Yail", "Yailianis", "Yaina", "Yaindhi", "Yaineliz", "Yair", "Yaira", "Yairaliz", "Yaire", "Yairelis", "Yaireliz", "Yairelys", "Yairon", "Yaisha", "Yaitza", "Yajaira", "Yaleidy", "Yaleishka", "Yalexis", "Yalianis", "Yalimar", "Yamaira", "Yamaris", "Yamil", "Yamila", "Yamilet", "Yamileth", "Yamilette", "Yamilex", "Yamiliz", "Yamilka", "Yamir", "Yamirelis", "Yamniel", "Yamuel", "Yan", "Yanaira", "Yancarlos", "Yancel", "Yandaniel", "Yandel", "Yandeliz", "Yandiel", "Yandre", "Yandriel", "Yaneira", "Yaneisha", "Yaneishka", "Yanelis", "Yaneliz", "Yanelys", "Yaneris", "Yangel", "Yaniel", "Yanielis", "Yanieliz", "Yanielys", "Yaniliz", "Yanira", "Yaniris", "Yanishka", "Yanitza", "Yankiel", "Yanluis", "Yanmanuel", "Yann", "Yannick", "Yanniel", "Yansel", "Yansiel", "Yanuel", "Yanxiel", "Yanzel", "Yanziel", "Yaphet", "Yara", "Yaraliz", "Yared", "Yareilys", "Yarel", "Yarelis", "Yareliz", "Yarell", "Yarelys", "Yarian", "Yariana", "Yarianis", "Yariann", "Yarianys", "Yaribel", "Yariel", "Yarielis", "Yarieliz", "Yariely", "Yarielys", "Yarilis", "Yariliz", "Yarilys", "Yarimar", "Yaritza", "Yashira", "Yasiel", "Yasmarie", "Yasmin", "Yasser", "Yatniel", "Yatziel", "Yavian", "Yaviel", "Yavielis", "Yavier", "Yaxel", "Yaxiel", "Yazid", "Yaziel", "Yazleemar", "Yazmin", "Yean", "Yediel", "Yedrian", "Yedrick", "Yedriel", "Yedziel", "Yeidaliz", "Yeiden", "Yeidiel", "Yeidimar", "Yeidriel", "Yeidy", "Yeika", "Yeilian", "Yeilianis", "Yeilianys", "Yeimarie", "Yeiniel", "Yeiren", "Yeisha", "Yeishka", "Yeiza", "Yelian", "Yelianis", "Yelianys", "Yeliel", "Yelier",
    "Yelimar", "Yelitza", "Yendiel", "Yendrick", "Yendriel", "Yeniel", "Yenielis", "Yenniel", "Yensen", "Yensiel", "Yenuel", "Yenxiel", "Yenzel", "Yenziel", "Yerai", "Yeralis", "Yeray", "Yerick", "Yeriel", "Yerielis", "Yerieliz", "Yerielys", "Yerik", "Yerika", "Yesenia", "Yeshua", "Yesiel", "Yeslian", "Yeslie", "Yesmarie", "Yesmary", "Yetsiel", "Yetxiel", "Yetzael", "Yetzel", "Yetziel", "Yeudiel", "Yexeira", "Yexian", "Yexiel", "Yeziel", "Yian", "Yinelis", "Yizette", "Yodalis", "Yolanda", "Yolianis", "Yolimar", "Yolivette", "Yolymar", "Yomaira", "Yomar", "Yomarie", "Yomaris", "Yometh", "Yonel", "Yoniel", "Yonuel", "Yoriel", "Yosef", "Yoshua", "Yoskar", "Yosniel", "Yosue", "Yosuel", "Young", "Yovaniel", "Yovanka", "Yuan", "Yuleidy", "Yuleisi", "Yuleisy", "Yuleizy", "Yulian", "Yuliana", "Yulianis", "Yulianna", "Yulissa", "Yulitza", "Yumalai", "Yuniel", "Yvanna", "Zabdiel", "Zachary", "Zadkiel", "Zadquiel", "Zael", "Zafira", "Zahara", "Zahid", "Zahir", "Zahira", "Zaid", "Zaida", "Zair", "Zamira", "Zara", "Zarah", "Zariel", "Zashenka", "Zayden", "Zenaida", "Zhavia", "Zion", "Zoe", "Zoelis", "Zoely", "Zoelys", "Zoey", "Zoralys", "Zoraya", "Zorielys", "Zorimar", "Zuheily", "Zuleika", "Zuleima", "Zuleimy", "Zuleyka", "Zuliany", "Zulianys", "Zulimar", "Zulmari", "Zulmarie", "Zulymar", "Zuriel", "Zurielys", "Zurisadai", "Zyan"
    "Yasamin","Sorawit","Tayyebeh","Giryes","Alireza","Carrington","Akbari","Takaki","Dinesh","Arsomngern","Maninis","Azim","Kazuhiro","Stephan","Junsuk","Ebrahimi","Zamir","Ramos","Washington","Elezi","Baldwin","Seong","Chadebec","Bruce","Kumawat","Teneggi","Saharia","Unal","Alfarra","Rewatbowornwong","Uzun","Bessadok","Hirose","Aleix","Naseer","Honari","Qayyum","Javed","Furnari","Kapidis","Coskun","Eadom","Northcutt","Nagar","Giuseppe","Belkhouja","Chattopadhyay0","Phongthawee","Mallis","Saengkyongam","Masuyama","Jafarian"]

# Filter out authors that don't match common English surnames
potential_chinese_authors = [(title, author) for title, author in titles_and_authors_alternative if not any(surname in author for surname in common_surnames)]

import pandas as pd

# Create a dataframe from the extracted data
df = pd.DataFrame(potential_chinese_authors, columns=['Title', 'First Author'])

# Save the dataframe to an Excel file
output_path = "./filtered_titles_and_authors.xlsx"
df.to_excel(output_path, index=False)
