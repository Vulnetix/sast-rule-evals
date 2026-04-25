<?php
// Triggers VNX-PHP-022: PHP open redirect via non-literal redirect destination

// UNSAFE: redirect destination comes from user input
$url = $_GET['next'];
header('Location: ' . $url);
exit;

// UNSAFE: Symfony controller redirect with variable
class AuthController extends AbstractController
{
    public function login(Request $request): Response
    {
        $redirectUrl = $request->query->get('redirect');
        // UNSAFE: non-literal URL passed to redirect()
        return $this->redirect($redirectUrl);
    }
}

// UNSAFE: Laravel redirect with user input
class HomeController extends Controller
{
    public function redirectAfterLogin(Request $request)
    {
        $target = $request->input('return_url');
        // UNSAFE: user-controlled URL
        return Redirect::to($target);
    }
}
