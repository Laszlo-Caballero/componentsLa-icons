import { FC, SVGProps } from "react";

export const LastRightIcon: FC<SVGProps<SVGSVGElement>> = ({ ...props }) => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" {...props}>
    <path
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={1.5}
      d="M5 18V6m14 0v12L9 12l10-6Z"
    />
  </svg>
);
