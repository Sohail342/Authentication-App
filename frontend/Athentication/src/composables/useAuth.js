import { ref } from "vue";
import axios from "axios";

export default function useAuth() {
  const user = ref(null);
  const token = ref(null);
  const error = ref(null);
  const loading = ref(false);

  const login = async (email, password) => {
    loading.value = true;
    error.value = null;

    try {
      const response = await axios.post("http://127.0.0.1:9000/user/login/", {
        email,
        password,
      });


      // Store the user token and optional user data
      token.value = response.data.token;
      user.value = { email };

      // Store token in localStorage for persistence
      localStorage.setItem("authToken", token.value);

      return response.data.msg;
    } catch (err) {
      if (err.response) {
        // Check if there is a response and error message
        if (err.response.status === 401) {
          // Handle authentication failure
          error.value = err.response.data.errors[0] || "Invalid credentials";
        } else {
          // Handle other errors (network, server, etc.)
          error.value = "An unknown error occurred";
        }
      } else {
        // If no response from the server (e.g., network error)
        error.value = "Network error, please try again later.";
      }
    } finally {
      loading.value = false;
    }
  };

  const logout = () => {
    user.value = null;
    token.value = null;
    localStorage.removeItem("authToken");
  };

  return {
    user,
    token,
    error,
    loading,
    login,
    logout,
  };
}
