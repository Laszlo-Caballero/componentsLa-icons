import { FC, SVGProps } from "react";

export const ArrowDown: FC<SVGProps<SVGSVGElement>> = ({ ...props }) => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" {...props}>
    <path fill="currentColor" d="M0 0h48v48H0z" />
    <path d="M24 29.171 9.414 14.585l-2.828 2.828L24 34.827l17.414-17.414-2.828-2.828z" />
  </svg>
);
