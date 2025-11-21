from django.shortcuts import redirect
from django.conf import settings
import re


class LoginRequiredMiddleware:
    """
    Middleware para forzar login en todas las vistas, excepto las exentas.
    Lee la lista de URLs exentas desde settings:
      - `LOGIN_EXEMPT_URLS` (recomendado)
      - si no existe, acepta `LOGIN_REDIRECT_URL_EXCEPTIONS` (tu nombre actual)
    """
    def __init__(self, get_response):
        self.get_response = get_response
        configured = getattr(settings, 'LOGIN_EXEMPT_URLS', None)
        if configured is None:
            configured = getattr(settings, 'LOGIN_REDIRECT_URL_EXCEPTIONS', [])

        exempt = [str(settings.LOGIN_URL)] + [str(u) for u in configured]

        # Compilar las entradas como expresiones regulares.
        # Si una entrada parece una ruta literal (no contiene metacaracteres),
        # la convertimos a un regex que coincida con el inicio: r'^/ruta(/|$)'
        compiled = []
        meta = set('.^$*+?{}[]\\|()')
        for u in exempt:
            # evitar duplicados
            if any(u == c.pattern for c in compiled):
                continue
            if any(ch in meta for ch in u):
                # ya contiene meta, compilar directamente
                try:
                    compiled.append(re.compile(u))
                except re.error:
                    # si falla la compilación, usar reconstrucción segura
                    compiled.append(re.compile(re.escape(u)))
            else:
                # literal path -> start-anchored regex
                pattern = r'^' + re.escape(u) + r'($|/)'
                compiled.append(re.compile(pattern))

        self.exempt_urls = compiled

    def __call__(self, request):
        path = request.path_info
        if not request.user.is_authenticated and not any(r.match(path) for r in self.exempt_urls):
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
