import sqlite3,os
from bottle import route,get, run, debug, template, request, static_file, error, TEMPLATE_PATH

# only needed when you run Bottle on mod_wsgi
#from bottle import default_app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "contact.db")
print "DB_PATH:" , db_path

#conn = sqlite3.connect(db_path)

#TEMPLATE_PATH.insert(0, '/home/chopeace/weekly/exer8')
TEMPLATE_PATH.insert(0, BASE_DIR)

@get('/<filename:re:.*\.tpl>')
def javascripts(filename):
        return static_file(filename, root='/home/chopeace/weekly/exer8')

@route('/')
def contact_list():


    #conn = sqlite3.connect('todo.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT id, firstname,lastname,email,phone,notes FROM contact;")
    result = c.fetchall()
    c.close()

    output = template('list_contact.tpl', rows=result)
    return output


@route('/<no:int>', method='GET')
def view_item(no):

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT id, firstname,lastname,email,phone,notes FROM contact WHERE id LIKE ?", (str(no)))
    cur_data = c.fetchone()

    return template('view_contact', old = cur_data, no = no)


@route('/new', method='GET')
def new_item():

    if request.GET.get('save','').strip():

        print "new: ", db_path
        firstname = request.GET.get('first_name', '').strip()
        lastname = request.GET.get('last_name', '').strip()
        email = request.GET.get('email', '').strip()
        phone = request.GET.get('phone', '').strip()
        notes = request.GET.get('notes', '').strip()

        conn = sqlite3.connect(db_path)

        c = conn.cursor()

        c.execute("INSERT INTO contact (firstname,lastname,email,phone,notes) VALUES (?,?,?,?,?)", (firstname,lastname,email,phone,notes))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new contact was inserted into the database, the ID is %s</p>\n <a href="/peace/exer8">List of people</a> ' % new_id
    else:
        return template('new_contact.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():

        firstname = request.GET.get('first_name', '').strip()
        lastname = request.GET.get('last_name', '').strip()
        email = request.GET.get('email', '').strip()
        phone = request.GET.get('phone', '').strip()
        notes = request.GET.get('notes', '').strip()

        print "save edit:?,db_path:?", (no,db_path)
        conn = sqlite3.connect(db_path)
        print "save edit: db connected"

        c = conn.cursor()
        c.execute("UPDATE contact SET firstname = ?, lastname = ?, email =?, phone= ?, notes=? WHERE id LIKE ?", (firstname,lastname,email,phone,notes,no))
        conn.commit()

        return '<p>The contact id %s was successfully updated</p>\n <a href="/peace/exer8">List of people</a> | <a href="/peace/exer8/%s">View Contact</a> ' %(no,no)

    else:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT id, firstname,lastname,email,phone,notes FROM contact WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_contact', old = cur_data, no = no)

@route('/item<item:re:[0-9]+>')
def show_item(item):

        #conn = sqlite3.connect('todo.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT firstname FROM contact WHERE id LIKE ?", (item))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'contact: %s' %result[0]

@route('/help')
def help():

    static_file('help.html', root='.')

@route('/json<json:re:[0-9]+>')
def show_json(json):

    #conn = sqlite3.connect('todo.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT firstname FROM contact WHERE id LIKE ?", (json))
    result = c.fetchall()
    c.close()

    if not result:
        return {'contact':'This item number does not exist!'}
    else:
        return {'contact': result[0]}


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


#debug(True)
#run(reloader=True)
#remember to remove reloader=True and debug(True) when you move your application from development to a productive environment
