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
      const response = await axios.post("http://127.0.0.1:8000/user/login/", {
        email,
        password,
      });

      // Store the user token and optional user data
      token.value = response.data.token;
      user.value = { email }; // or fetch additional user details if necessary

      // Store token in localStorage for persistence
      localStorage.setItem("authToken", token.value);

      return response.data.msg; // Return success message
    } catch (err) {
      error.value = err.response?.data?.errors.non_field_errors || ["Login failed"];
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
