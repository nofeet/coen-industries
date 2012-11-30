"""Middleware to parse and apply merchant's name from path's subdomain.""" 


class SubdomainMiddleware(object):

    def process_request(self, request):
        """Parse and add merchant's name from path's subdomain to path_info."""
        request.subdomain = ""
        http_host = request.META.get("HTTP_HOST", "")
        sub_chunks = http_host.replace("www.", "").lower().split(".")[:-2]
        if sub_chunks:
            subdomain = "_".join(sub_chunks)
            request.subdomain = subdomain
