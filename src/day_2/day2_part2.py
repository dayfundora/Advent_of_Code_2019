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

def intcode_inverse_list_comprehension(fileName):
        noun,verb = [(i,j+i) for i in range(100) for j in range(100-i) if intcode(fileName,[(1,i),(2,j+i)])[0]==19690720][0]
        return noun,verb


def intcode_inverse(fileName):
        for i in range(100):
                for j in range(100-i):
                        codes=intcode(fileName,[(1,i),(2,j+i)])
                        if(codes[0]==19690720):
                                noun=i
                                verb=j+i
        return noun,verb

if __name__ == '__main__':
        noun,verb=intcode_inverse_list_comprehension('input.txt')
        print(100*noun+verb)
        #3146