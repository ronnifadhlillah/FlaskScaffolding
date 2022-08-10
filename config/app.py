[Application]
  AppName=Scaffolding
  Debug=True
  Environment=development
  Timezone=UTC
  Locale=id
  FallbackLocale=en
  SecretKey=b'\xf3\xacD\x07I\x07d\x05}{\xf5\xa0M6.\x1c\xff?.\x8d\xa2\xbe\xaeW'

[URI]
# For development in different port or url
  Set=False
  Url=127.0.0.1
  Port=3000

[BootStrap]
  Template=views
  Static=public
  Router=route
