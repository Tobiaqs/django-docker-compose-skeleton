FROM nginxproxy/nginx-proxy
RUN sed -i -s 's/server {{ \$containerNetwork\.IP }}\:{{ \$address\.Port }}\;/server {{ \$containerNetwork\.IP }}\:{{ \$address\.Port }}\ fail_timeout=1s;/g' /app/nginx.tmpl
