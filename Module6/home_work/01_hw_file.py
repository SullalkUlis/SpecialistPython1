# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    def log(text, file="log.txt"):
    path = 'Data/' + str(file).strip()
    f = open(path, 'a', encoding='UTF-8')
    str_out = str(text) + '\n'
    f.write(str_out)
    f.close()


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
