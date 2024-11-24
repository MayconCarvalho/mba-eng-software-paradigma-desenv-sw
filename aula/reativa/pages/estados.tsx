import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import { useState, useEffect } from "react"; // Importa o hook useState

function ContadorComMensagem() {
  const [contador, setContador] = useState(0); // Inicializa o estado contador com 0

  // Função que é executada toda vez que o contador é atualizado
  useEffect(() => {
    console.log("O contador foi atualizado para", contador);
  }, [contador]);

  const incrementar = () => {
    setContador(contador + 1); // Incrementa o contador
  };

  // Função que incrementa o contador
  return (
    <main className={styles.main}>
      <p className={styles.aula}>Você clicou {contador} vezes </p>
      <button className={styles.button} onClick={incrementar}>
        Clique aqui
      </button>
    </main>
  );
}

export default ContadorComMensagem;
