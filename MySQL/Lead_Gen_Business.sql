-- What query would you run to get the total revenue for March of 2012?
SELECT SUM(billing.amount) AS 'March Revenue', billing.charged_datetime AS 'March 2012' 
FROM billing 
WHERE billing.charged_datetime LIKE '%2012-03%';

-- What query would you run to get total revenue collected from the client with 
-- an id of 2?
SELECT billing.client_id, SUM(billing.amount) AS 'Total Revenue Collected'
FROM billing
WHERE billing.client_id = 2;

-- What query would you run to get all the sites that client=10 owns?
SELECT sites.client_id, GROUP_CONCAT(' ',sites.domain_name) AS 'domain'
FROM sites
WHERE sites.client_id = 10
GROUP BY sites.client_id;

-- What query would you run to get total # of sites created each month for the 
-- client with an id of 1? What about for client=20?
SELECT sites.client_id, COUNT(sites.domain_name) AS 'Number of Domains', MONTH(sites.created_datetime) AS 'Month'
FROM sites
WHERE sites.client_id = 1
GROUP BY MONTH(sites.created_datetime);

SELECT sites.client_id, COUNT(sites.domain_name) AS 'Number of Domains', MONTH(sites.created_datetime) AS 'Month'
FROM sites
WHERE sites.client_id = 20
GROUP BY MONTH(sites.created_datetime);

-- What query would you run to get the total # of leads we've generated for each 
-- of our sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name AS Website, COUNT(leads.leads_id) AS 'Number of Leads', DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS 'Dates Created'
FROM leads
JOIN sites ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-03-15'
GROUP BY leads.site_id
ORDER BY MONTH(leads.registered_datetime), DATE(leads.registered_datetime);

-- What query would you run to get a list of client names and the total # of leads 
-- we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS 'Client Name', COUNT(leads.leads_id) AS '# of Leads', DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS 'Dates Created'
FROM clients
JOIN sites ON clients.client_id = sites.client_id 
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY leads.site_id
ORDER BY MONTH(leads.registered_datetime), DATE(leads.registered_datetime);

-- What query would you run to get a list of client name and the total # of leads 
-- we've generated for each client each month between month 1 - 6 of Year 2011?
SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS 'Client Name', COUNT(leads.leads_id) AS '# of Leads', DATE_FORMAT(leads.registered_datetime, '%M %Y') AS 'Dates Created'
FROM clients
JOIN sites ON clients.client_id = sites.client_id 
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY leads.site_id
ORDER BY MONTH(leads.registered_datetime);

-- What query would you run to get a list of client name and the total # of leads 
-- we've generated for each of our client's sites between January 1, 2011 to December 31, 2011?
--  Come up with a second query that shows all the clients, the site name(s), and 
-- the total number of leads generated from each site for all time.
SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS 'Client Name', sites.domain_name AS Website, COUNT(leads.leads_id) AS '# of Leads', DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS 'Dates Created'
FROM clients
JOIN sites ON clients.client_id = sites.client_id 
JOIN leads ON leads.site_id = sites.site_id 
WHERE leads.registered_datetime BETWEEN '2011-01-1' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.last_name, (leads.registered_datetime), DAY(leads.registered_datetime), YEAR(leads.registered_datetime);

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS 'Client Name', sites.domain_name AS Website, COUNT(leads.leads_id) AS '# of Leads'
FROM clients
JOIN sites ON clients.client_id = sites.client_id 
JOIN leads ON leads.site_id = sites.site_id 
GROUP BY sites.domain_name
ORDER BY clients.last_name, (leads.registered_datetime), DAY(leads.registered_datetime), YEAR(leads.registered_datetime);

-- Write a single query that retrieves total revenue collected from each client 
-- each month of the year.
SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS 'Client Name', SUM(billing.amount) AS 'Total Revnue Collected', DATE_FORMAT(billing.charged_datetime, '%M') AS 'Month', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'Year'
from clients
JOIN billing ON billing.client_id = clients.client_id
GROUP BY clients.first_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime);

-- Write a single query that retrieves all the sites that each client owns. 
-- Group the results so that each row shows a new client. Add a new field called 
-- 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS 'Client Name', GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') AS 'sites'
from clients
JOIN sites ON sites.client_id = clients.client_id 
GROUP BY clients.last_name

