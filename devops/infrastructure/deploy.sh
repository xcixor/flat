#!/usr/bin/env bash

set -o errexit
set -o pipefail
# set -o xtrace

get_var(){
    local name="$1"
    curl -s -H "Metadata-Flavor: Google" \
    "http://metadata.google.internal/computeMetadata/v1/instance/attributes/${name}"
}

get_required_variables () {
    export IP_ADDRESS="$(get_var "ip_address")"
    ENVIRONMENT="$(get_var "django_environment")"
    export DJANGO_SETTINGS_MODULE=core.settings.${ENVIRONMENT}
    export SECRET_KEY="$(sudo openssl rand -hex 64)"
    export DATABASE_NAME="$(get_var "database_name")"
    export DATABASE_USER="$(get_var "database_user")"
    export DATABASE_PASSWORD="$(get_var "database_password")"
    export POSTGRES_IP="$(get_var "postgres_ip")"
    export APPLICATION_HOST="$(get_var "application_host")"
    export GITHUB_BRANCH="$(get_var "github_branch")"
    export NGINX_SERVER_NAME="${APPLICATION_HOST}"
    export SERVICE_ACCOUNT="$(get_var "gs_credentials")"
    export ADMIN="$(get_var "admin")"
    export ADMIN_PASSWORD="$(get_var "admin_password")"
    export ADMIN_EMAIL="$(get_var "admin_email")"
}

install_postgres(){
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
}

configure_postgres_db(){
    sudo su postgres
    psql
    CREATE DATABASE ${DATABASE_NAME};
    CREATE USER ${DATABASE_USER} WITH PASSWORD ${DATABASE_PASSWORD};
    GRANT ALL PRIVILEGES ON DATABASE ${DATABASE_NAME} to ${DATABASE_USER};
    \q
    exit
}

clone_repository() {
    cd ~
    if [ "${GITHUB_BRANCH}" ]; then
        git clone -b "${GITHUB_BRANCH}" https://github.com/xcixor/flat.git
    else
        git clone https://github.com/xcixor/flat.git
    fi
    cd flat
}

copy_nginx_conf() {
    envsubst '\$NGINX_SERVER_NAME' < ~/flat/devops/deployment_scripts/nginx.conf > /etc/nginx/conf.d/nginx.conf
}

copy_supervisord_conf () {
    sudo cp ~/flat/devops/deployment_scripts/supervisord.conf /etc/supervisor/supervisord.conf
    sudo cp ~/flat/devops/deployment_scripts/start.sh /usr/local/bin/start-app
    sudo chmod +x /usr/local/bin/start-app
}

configure_pelly_website() {
    pipenv lock -r >requirements.txt
    pip3 install -r requirements.txt
    python3 ~/flat/src/core/manage.py makemigrations
    python3 ~/flat/src/core/manage.py migrate
    python3 ~/flat/src/core/manage.py collectstatic --no-input
    sudo systemctl restart supervisor
    sudo nginx -s reload
}

create_superuser(){
    # echo "from django.contrib.auth.models import User; User.objects.create_superuser(os.environ.get('ADMIN'), os.environ.get('ADMIN_EMAIL'), os.environ.get('ADMIN_PASSWORD'))" | python3 ~/flat/src/core/manage.py shell
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or \
                User.objects.create_superuser(os.environ.get('ADMIN'), os.environ.get('ADMIN_EMAIL'), os.environ.get('ADMIN_PASSWORD'))" \
                | python3 ~/flat/src/core/manage.py shell
}

main (){
    get_required_variables
    # install_postgres
    # configure_postgres_db
    clone_repository
    copy_nginx_conf
    copy_supervisord_conf
    configure_pelly_website
    create_superuser
}

main