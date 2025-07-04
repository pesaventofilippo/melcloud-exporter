# melcloud-exporter
A simple Prometheus exporter for MELCloud Air-To-Air Heat Pumps.

### Description
This is a very basic Prometheus exporter for [MELCloud](https://app.melcloud.com) air-to-air heat pumps that gathers device data from the internet.

## Usage
The exporter is configured using environment variables.  

| Variable            | Description                       | Default      |
|---------------------|-----------------------------------|--------------|
| `PROMETHEUS_PORT`   | Port the exporter listens on      | `8000`       |
| `PROMETHEUS_PREFIX` | Prefix for the Prometheus metrics | `"melcloud"` |
| `USERNAME`          | MELCloud Login username           | -            |
| `PASSWORD`          | MELCloud Login password           | -            |

## Docker
The exporter is available as a Docker image on the [GitHub Container Registry](https://ghcr.io/pesaventofilippo/melcloud-exporter).

To run the exporter using Docker, you can use the following command:
```bash
docker run -d -p 8000:8000 \
    -e USERNAME=user@example.com \
    -e PASSWORD=yourpassword \
    ghcr.io/pesaventofilippo/melcloud-exporter
```

### docker compose
You can also use `docker compose` to run the exporter.
Here is an example `compose.yml` file:
```yaml
services:
  melcloud-exporter:
    image: ghcr.io/pesaventofilippo/melcloud-exporter
    ports:
      - 8000:8000
    environment:
      - USERNAME=user@example.com
      - PASSWORD=yourpassword
```
