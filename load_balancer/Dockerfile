# Dockerfile for Nginx Load Balancer //May not be needed
FROM alpine:latest
RUN apk add --no-cache nginx
RUN mkdir -p /run/nginx
COPY nginx.cfg /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
