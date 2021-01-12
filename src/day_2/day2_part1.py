def readFile(fileName):
        fileObj=open(fileName,"r")
        inputs=fileObj.read().replace("\n","").split(',')
        fileObj.close()
        return inputs

def restore_program(intcode_list, values):
                for val in values:
                        intcode_list[val[0]]=val[1]

def code_1(intcode_list, index):
        try:
                intcode_list[intcode_list[index+3]]=intcode_list[intcode_list[index+1]]+intcode_list[intcode_list[index+2]]   
        except:
                print("Elfo, este código no esta bien formulado, no hay suficiente valores para realizar el código, ¡¡Ya me moleste, no computo más!!")
                
def code_2(intcode_list, index):
        try:
                intcode_list[intcode_list[index+3]]=intcode_list[intcode_list[index+1]]*intcode_list[intcode_list[index+2]]   
        except:
                print("Elfo, este código no esta bien formulado, no hay suficiente valores para realizar el código, ¡¡Ya me moleste, no computo más!!")

def intcode(fileName, restore_values=[], size=4):
        intcode_list=[int(i) for i in readFile(fileName)]
        restore_program(intcode_list,restore_values)
        
        index=0
        while index<len(intcode_list):
                if intcode_list[index]==1:
                        code_1(intcode_list, index)
                elif intcode_list[index]==2:
                        code_2(intcode_list, index)
                elif intcode_list[index]==99:
                        break
                else:
                        raise Exception("Elfo, el código "+str(intcode_list[index])+" no lo reconozco, ¡¡Ya me moleste, no computo más!!")
                index+=size
        return intcode_list

if __name__ == '__main__':
        codes = intcode('input.txt',[(1,12),(2,2)])
        print(codes[0])
        #8017076
