try:
    f = open('data\\testfile.txt')
    var = bad_var
except Exception:
    print('Sorry. This file does not exist')


try:
    f = open('data\\test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')


try:
    f = open('data\\testfile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


try:
    f = open('data\\test_file.txt')
    # print(f.read()) # trying to handle exception as specific as possible
    # f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()


try:
    f = open('data\\testfile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")


try:
    f = open('data\\corrupt_file.txt')
    if f.name == 'data\\corrupt_file.txt':
        raise Exception  # manually raises an exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
