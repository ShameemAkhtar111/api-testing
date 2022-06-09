

API_HOST = {
    "test": "http://localhost:8888/demosite/wp-json/wc/v3/",
    "dev": "",
    "prod": ""

}
WOO_API_HOST = {
    "test": "http://localhost:8888/demosite/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
        "test": {
            'host': 'localhost',
            'database': 'demosite',
            'table_prefix': 'wp_',
            'port': 8889,
            'socket': None
        },
        "dev": {


        },
        "prod": {

        }
    },

    'docker': {
        "test": {
            'host': 'host.docker.internal',
            'database': 'demosite',
            'table_prefix': 'wp_',
            'port': 8889,
            'socket': None
        },
        "dev": {


        },
        "prod": {

        }

    }


}