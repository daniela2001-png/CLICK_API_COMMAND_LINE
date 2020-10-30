from setuptools import setup


setup(
    # aqui le decimos como vamos ainvocra nuestar lien commnad osea con "pv"
    name='pv',
    version='0.1',
    py_modules=['pv'],
    # paquetes o librerias necesarias para nuestra mini api
    install_requires=[
        'Click',
    ],
    # le damos el punto de entrada de nuestra api que sera cli de pv
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)
