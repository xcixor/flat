#!/usr/bin/env bash

set -o errexit
set -o pipefail
# set -o nounset
# set -o xtrace

get_var() {
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
    export GS_BUCKET_NAME="$(get_var "gs_bucket")"
    export GS_BUCKET_URL="$(get_var "gs_bucket_url")"
    export GOOGLE_APPLICATION_CREDENTIALS="/usr/local/gs-account/account.json"
}

start_app () {
    cd ~/flat/src/core/
    gunicorn -b 0.0.0.0:8000 --error-logfile /var/log/gathee-error.log core.wsgi
}

main () {
    get_required_variables
    start_app
}

main "$@"
