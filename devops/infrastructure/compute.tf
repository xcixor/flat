data "google_compute_zones" "available" {}

resource "google_compute_instance" "name" {
  project      = "${var.project}"
  zone         = "${var.zone}"
  name         = "${var.compute_instance_name}"
  machine_type = "${var.machine_type}"
  tags = ["${var.firewall}-https-firewall", "${var.firewall}-ssh-firewall", "${var.firewall}-http-firewall"]

  boot_disk {
    initialize_params {
      image = "${var.image_name}"
    }
  }

  network_interface {
    network = "default"

    access_config {
      nat_ip = "${var.ip_address}"
      network_tier = "STANDARD"
    }
  }

  metadata_startup_script = "${file("deploy.sh")}"

  metadata = {
    ip_address    = "${var.ip_address}"
    database_name = "${var.database_name}"
    database_user         = "${var.database_user}"
    database_password     = "${var.database_password}"
    postgres_ip   = "${var.postgres_ip}"
    gs_bucket = "${var.gs_bucket}"
    gs_bucket_url = "${var.gs_bucket_url}"
    django_environment = "${var.django_environment}"
    application_host = "${var.application_host}"
    github_branch = "${var.github_branch}"
    gs_credentials = "${file("../account/account.json")}"
    admin = "${var.admin}"
    admin_email = "${var.admin_email}"
    admin_password = "${var.admin_password}"
  }

}
