
def create_table():
    queries = [
        'CREATE TABLE IF NOT EXISTS users (\
                user_id SERIAL PRIMARY KEY,\
                first_name VARCHAR(30),\
                last_name VARCHAR(30),\
                username VARCHAR(30),\
                email VARCHAR(255),\
                password VARCHAR(255)\
                )',
    
        'CREATE TABLE IF NOT EXISTS questions (\
                question_id SERIAL PRIMARY KEY,\
                title VARCHAR(255),\
                content VARCHAR(500),\
                user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE,\
                posted_date TIMESTAMP)',

        'CREATE TABLE IF NOT EXISTS answers (\
                answer_id SERIAL PRIMARY KEY,\
                answer_body VARCHAR(500),\
                question_id INTEGER REFERENCES questions (question_id) ON DELETE CASCADE,\
                posted_date TIMESTAMP,\
                accepted BOOLEAN DEFAULT false,\
                user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE)',
                     
      
        'CREATE TABLE IF NOT EXISTS tokens (\
                token_id SERIAL PRIMARY KEY,\
                token VARCHAR(200)\
                )'
    
    ]
        
    return queries
