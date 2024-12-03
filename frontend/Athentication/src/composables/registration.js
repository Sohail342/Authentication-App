import { ref } from "vue";
import axios from "axios";

export default function user_register() {
  const user = ref(null);
  const token = ref(null);
  const error = ref(null);
  const loading = ref(false);

  const register = async (email, password, name, password2, terms_conditions) => {
    loading.value = true;
    error.value = null;

    try {
      const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:9000";
      const response = await axios.post(`${API_BASE_URL}/user/register/`, {
        email,
        name,
        password,
        password2,
        terms_conditions,
      });

      token.value = response.data.token;
      user.value = { email };

      localStorage.setItem("authToken", token.value);

      return response.data.msg;
    } catch (err) {
      error.value =
        err.response?.data?.detail || err.response?.data?.message || "An error occurred during registration.";
    } finally {
      loading.value = false;
    }
  };

  return {
    user,
    token,
    error,
    loading,
    register,
  };
}
