# Interaction Tree

Task 0: minimal FastAPI deployment on Oracle Linux OCI. No payment, QR, or database implementation.

## Local run

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
curl --fail http://127.0.0.1:8000/health
```

Expected response: `{"status":"ok"}`.

## Deployment layout

- `/opt/interaction-tree`: Git checkout and Python virtual environment
- `interaction-tree`: unprivileged runtime user
- `deploy/interaction-tree.service`: systemd unit, listening only on loopback port 8000
- Caddy: public HTTP/HTTPS reverse proxy; install the approved host in `/etc/caddy/Caddyfile`
- OCI ingress: web ports 80/443; SSH 22 should be restricted to the administrator's IP
- Keep SSH private keys and account credentials outside this repository.

## Operations (on the VM)

```sh
sudo systemctl status interaction-tree caddy
sudo systemctl restart interaction-tree
sudo journalctl -u interaction-tree -n 100 --no-pager
sudo journalctl -u caddy -n 100 --no-pager
sudo systemctl enable interaction-tree caddy
```

## Apply a Git update (on the VM)

Run as the checkout owner after pushing changes to GitHub:

```sh
cd /opt/interaction-tree
git pull --ff-only origin main
.venv/bin/pip install -r requirements.txt
sudo systemctl restart interaction-tree
curl --fail http://127.0.0.1:8000/health
git rev-parse HEAD
```

Actual hostname settings belong in the ignored `.private/Caddyfile` or `deploy/Caddyfile`. Keep the tracked `deploy/Caddyfile.example` generic. The server uses `/etc/caddy/Caddyfile`.
