from django.shortcuts import redirect

def confirm_required(func):
    def wrapper(self, request):
        if not request.user.is_confirmed:
            return redirect('users:confirm', username=request.user.username)
        else:
            return func(self, request)
    return wrapper

def nologin_required(func):
    def wrapper(self):
        if str(self.user) == 'AnonymousUser':
            return func(self)
        else:
            return redirect('shop:index')
    return wrapper

def noconfirm_nologin_required(func):
    def wrapper(self, username):
        if str(self.user) == 'AnonymousUser':
            return redirect('users:login')
        if not self.user.is_confirmed:
            return func(self, username)
        return redirect('shop:index')
    return wrapper