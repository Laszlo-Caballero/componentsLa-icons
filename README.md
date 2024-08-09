# Components La icons

Libreria de componentes de react basado en **Material Ui**,
creado con el hecho de aprender a hacer una libreria y usarlo en mis
proximos proyectos

## Instalacion

- npm

```bash
  npm install componentsla-icons
```

- pnpm

```bash
  pnpm install componentsla-icons
```

## Uso

```tsx
import { CopyIcon } from "componentsla-icons";

export default function Page() {
  return (
    <div>
      <CopyIcon width={20} height={20} color="#FFFFFF" />
    </div>
  );
}
```

## Aportar

1. Clonar proyecto

```bash
  git clone https://github.com/Laszlo-Caballero/componentsLa-icons.git
```

2. Instalar dependencias

```bash
  npm install
```

3. Compilar proyecto

```bash
  npm run build
```

### TODOS

- Iconos
  - [ ] Añadir iconos
  - [x] Ponerlos en un solo archivo ⚠️
  - [x] Poner prop de color en hexadecimal
