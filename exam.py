class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name

    def get_data(self):
        #metodo che deve tornare una lista di lista
        #apro il file
        my_file=open(self.name, 'r')

        lista_elementi=[] #inizializzo una lista vuota
        
        for line in my_file:
            #leggo il file riga per riga
            elements=line.split(',')
            #faccio lo split di ogni riga sulla virgola, in modo che mi torni una lista che abbia come primo elemento la data e secondo il numero dei passseggeri

            # pulisco il carattere di newline e gli spazi di inizio e fine stringa
            elements[-1] = elements[-1].strip()
            
            if elements[0] != 'date':
            #se non sto processando l'intestazione, associo gli elementi
                data=elements[0]
                elements[1]=float(elements[1])
                valore=elements[1]

                #converto la stringa 'passengers', ossia il secondo elemento della lista 'elements', in numero con la funzione float()

                lista_elementi.append(elements)
                #aggiungo gli elementi sottoforma di lista nella lista inizializzata precedentemente

                
        print(lista_elementi) #temporaneo
        return lista_elementi

              
#def compute_avg_monthly_difference(time_series, first_year, last_year):
    #serie storica=data.csv
    #primo anno=data anno
    #terzo anno=data primo anno +2
    
time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()
