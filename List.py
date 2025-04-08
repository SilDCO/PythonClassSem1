#pets = ["Salem", "Pandora", "Lupin", "Akira"] #lista de variaveis
#index = int(input("Whats the name of your pet: "))

#myfavoritethings= ["cats", "coffee" , 8, 4, "college", "Brazil", True] #primeiro elemento sempre zero

#print ("My pets in Brazil:",pets) #vai mostrar a lista
#print ("My pets in Brazil:",pets[0]) #vai mostrar na tela o primeiro pet

#pets[0]= "Garfield" #substitui o item que esta na ordem indicada

#print (pets) #mostra com a substituicao

#pets[1] = pets[3] # copia os valores 

#print (pets) # print com a alteracao

#print (pets[index]) #imprime na tela a ordem colocada pelo usuario

#print (pets[(index-1)])

#print ("How many cats do you have? ", len(pets)) # mostra a quantidade de elementos no grupo

#del pets[0]
#pets.append("Salem") #para adicionar mais itens a lista
#pets.append(input("Tell me another pets that you have:"))
#print ("How many cats you have? ", len(pets))
#print (pets)

#pets.insert(0,"Rabicho")

#print(pets)

#Definição de lista
#Definição de algoritimo
#Print is a function
#delete is a instruction



#my_list = []
#for i in range(5):
   # my_list.insert(0, i + 1)

#print(my_list)

#listcolour = ["Black", "White", "Blue", "Grey", "Red"]

#for colour in range(5):
    #print(listcolour[colour])


#listcolour = ["black", "White" "blue", "Greuy"]
    #for colour in listcolour:
        #print(listcolour)
#lst = [1,2,3,4,5]
#lst_2 = []
#add = 0
#for number in lst:
    #add += number
    #lst_2.append(add)

#print(lst_2)

#lst = [1,2,3,4,5]
#lst_2 = []
#for number in lst:
    #add = 0
    #add += number
    #lst_2.append(add)
#print(lst_2)

#my_list = [8, 10, 6, 2, 4]  # list to sort
#swapped = True  # It's a little fake, we need it to enter the while loop.

#while swapped:
    #swapped = False  # no swaps so far
    #for i in range(len(my_list) - 1):
        #if my_list[i] > my_list[i + 1]:
            #swapped = True  # a swap occurred!
            #my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

#print(my_list)
#my_list = [8, 10, 6, 2, 4]  # Lista a ser ordenada
#swapped = True  # Variável de controle para verificar se houve trocas

#while swapped:
    #swapped = False  # Assume que nenhuma troca será feita
    #for i in range(len(my_list) - 1):  # Percorre a lista até o penúltimo elemento
        #if my_list[i] > my_list[i + 1]:  # Compara dois elementos vizinhos
            #my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Troca os elementos de posição
            #swapped = True  # Indica que houve uma troca, então precisamos repetir o processo

#print(my_list)  # Exibe a lista ordenada

#numbers = [5,3,2,4,7]
#swaped = True

#while swaped:
    #swaped = False
    #for i in range (len(numbers) - 1):
        #if numbers[i] > numbers [i+1]:
            #numbers[i], numbers [i+1] = numbers [i + 1], numbers [i]
            #swaped = True
#print(numbers)

#numbers = [3,5,8,7,9,6]
#swaped = True

#while swaped:
    #swaped = False
    #for i in range (len(numbers) - 1):
        #if numbers[i] < numbers [i + 1]:
            #numbers [i], numbers [i + 1] = numbers [i + 1] , numbers [i]
            #swaped = True
#print(numbers)

numbers = [3,5,8,7,9,6]
swaped = True

while swaped:
    swaped = False
    for i in range(len(numbers)-1):
        if numbers[i]< numbers [i - 1]:
            numbers [i] , numbers [i - 1] = numbers [i - 1] , numbers [i]
        else:
            numbers [i] > numbers [i + 1]
            numbers [i] , numbers [i + 1] = numbers [i + 1] , numbers [i]
            print(numbers)
            swaped = True
print(numbers)








