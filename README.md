
Web Magazine Application(Sketch)


/api/moderator/auth/login/
  - description:  moderator login method
  - param: 
  {
    'email': '<String>',
    'password': '<String>'
  }
/api/moderator/auth/logout/ 
  - description:  moderator logout method
  - param: 
  {}

/api/moderator/blogpost/<pk>/ 
  - description:  moderator retrieve blogpost by id

/api/moderator/blogpost/<pk>/confirm
  - description:  confirm blogpost
  - param: 
  {
    'is_confirmed': '<bool>'
  }

/api/moderator/blogpost/list/ 
  - description:  get blogpost list

/api/reporter/auth/login/ 
  - description:  reporter login method
  - param: 
  {
    'email': '<String>',
    'password': '<String>'
  }
/api/reporter/auth/logout/  
  - description:  reporter logout method
  - param: 
  {}

/api/reporter/blogpost/<pk>/  
  - description:  reporter retrieve blogpost by id
/api/reporter/blogpost/create/  
  - description:  reporter create blogpost
  - param: 
  {
    'body': '<String>',
    'title': '<String>'
  }

/api/reporter/blogpost/list/  
  - description:  get blogpost list
/api/reporter/profile/info/ 
  - description:  get  reporter profile info

# APi endpoints available without authorization
/api/public/blogpost/<pk>/  
  - description:  get blogpost by id
/api/public/blogpost/list/  
  - description:  get blogpost list
/api/public/blogpost/search/  
  - description:  search blogpost by text in title and body


P.S. this is demo for demonstration purposes,
    for using in production optimization must be done(
    -secure public end-points,
    -refine permissions with group
    -maybe use elastic search for search)

Author: Andrii Gerasymchuk
email: gera3dartist@gmail.com