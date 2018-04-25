# -*- coding: utf-8 -*-
import MySQLdb


HOST='bz3-m-db3.eng.vmware.com'
USERNAME='xxx'
PASSWORD='xxx'
DATABASE='bugzilla'
PORT=3306

BUG_LONG_DESCRIPTION = 'select bug_id, thetext from longdescs ' \
                        'where bug_id="1363581" ORDER BY bug_when;'

def get_data_from_bugzilla():
    try:
        connect = MySQLdb.connect(host=HOST, user=USERNAME, passwd=PASSWORD, db=DATABASE, port=PORT)
        cursor = connect.cursor()
        sql = '''SELECT bugs.bug_id, bugs.bug_severity, bugs.priority, bugs.bug_status, bugs.resolution,
map_assigned_to.login_name as assignee, map_reporter.login_name as reporter,
map_categories.name as category,
map_components.name as component,
bugs.short_desc

FROM bugs  INNER JOIN profiles AS map_assigned_to ON
(bugs.assigned_to = map_assigned_to.userid) INNER JOIN profiles AS map_reporter ON
(bugs.reporter = map_reporter.userid) INNER JOIN categories AS map_categories ON
(bugs.category_id = map_categories.id) INNER JOIN components AS map_components ON
(bugs.component_id = map_components.id) LEFT JOIN partners ON
(bugs.bug_id = partners.bug_id) LEFT JOIN partnerdefs AS map_partner ON
(partners.partner_id = map_partner.id) LEFT JOIN customers ON
(bugs.bug_id = customers.bug_id) LEFT JOIN customerdefs AS map_customer ON
(customers.customer_id = map_customer.id)

WHERE bugs.product_id IN (292) and map_assigned_to.login_name='branw'
LIMIT 100'''

        print sql
        cursor.execute(sql)
        data_fetched = cursor.fetchall()
        connect.close()
        
        return data_fetched
    except Exception as e:
        print e.msg
