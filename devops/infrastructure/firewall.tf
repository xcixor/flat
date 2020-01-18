resource "google_compute_firewall" "http-firewall" {
    project = "${var.project}"
    name    = "${var.firewall}-allow-http"
    network = "${var.network}"

    allow {
        protocol = "tcp"
        ports    = ["80"]
    }

    source_ranges = ["0.0.0.0/0"]
    target_tags   = ["${var.firewall}-http-firewall"]
}

resource "google_compute_firewall" "ssh-firewall" {
    project = "${var.project}"
    name    = "${var.firewall}-allow-ssh"
    network = "${var.network}"


    allow {
        protocol = "tcp"
        ports    = ["22"]
    }

    source_ranges = ["0.0.0.0/0"]
    target_tags   = ["${var.firewall}-ssh-firewall"]
}

resource "google_compute_firewall" "https-firewall" {
    project = "${var.project}"
    name    = "${var.firewall}-allow-https"
    network = "${var.network}"

    allow {
        protocol = "tcp"
        ports    = ["443"]
    }

    source_ranges = ["0.0.0.0/0"]
    target_tags   = ["${var.firewall}-https-firewall"]
}