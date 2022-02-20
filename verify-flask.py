##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
from flask import Flask, request, jsonify
from fnc.extractFeature import extractFeature
from fnc.matching import matching
from time import time
from path import image_database_path
from sys import argv, exit
from os.path import exists

##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Get the argument

# Flask api input

app = Flask(__name__)

@app.route('/verify',methods=['GET'])
def hello_world():
    d = {}
    d['Query'] = request.args['Query']

    filename = '%s%s' % (image_database_path, d['Query'])

    # Extract feature
    start = time()
    print(d['Query'])
    print('>>> Start verifying {}'.format(filename))
    template, mask, filename = extractFeature(filename)

    # Matching
    id_acc = matching(template, mask, 0.42)
    resp=''

    if id_acc == -1:
        print('>>> Error!')
        resp = '>>> Error!'

    elif id_acc == 0:
        print('>>> No matched!')
        resp = '>>> No matched!'

    else:
        print('>>> ID {} is matched!'.format(str(id_acc)))
        resp = 'ID {} is matched!'.format(str(id_acc))

    # Time measure
    end = time()
    print('>>> Verification time: {} [s]\n'.format(end - start))
    return resp


if __name__ == '__main__':
    app.run()
    # if len(argv) == 2:
    #     filename = '%s%s' % (image_database_path, argv[1])
    #     if not exists(filename):
    #         print(">>> Wrong file!\n")
    #         exit()
    # elif len(argv) == 1:
    #     filename = '%s104/104_1_1.jpg' % image_database_path
    #     print(argv)
    #     print(filename)
    # else:
    #     print(">>>Wrong syntax!\n")
    #     exit()

    # # Extract feature
    # start = time()
    # print(d['Query'])
    # print('>>> Start verifying {}'.format(filename))
    # template, mask, filename = extractFeature(filename)

    # # Matching
    # id_acc = matching(template, mask, 0.42)

    # if id_acc == -1:
    #     print('>>> Error!')

    # elif id_acc == 0:
    #     print('>>> No matched!')

    # else:
    #     print('>>> ID {} is matched!'.format(str(id_acc)))

    # # Time measure
    # end = time()
    # print('>>> Verification time: {} [s]\n'.format(end - start))
