# Blog Django
### Por Eric de Castro

Projeto de blog feito em Django.

- O projeto é focado no back-end, porém achei interessante apresentar um front-end bem feito
- Inicialmente o front-end era um template de bootstrap quase pronto, porém, ao longo do projeto, modifiquei praticamente todo o css, inclusive na parte de responsividade
- Utilizadas Class-based views
- Google Recaptcha implementado nos formulários de cadastro, login e comentários
- Módulo django-axes implementado para reforçar a segurança, sendo que se o usuário errar a senha mais de cinco vezes a conta é bloqueada
- Amazon S3 da AWS usado para armazenar as imagens
- Módulo python-decouple utilizado para esconder as secret keys do django, google recaptcha e S3 da Amazon
- Site hospedado no Heroku https://django-blog-ericdecastro.herokuapp.com/
