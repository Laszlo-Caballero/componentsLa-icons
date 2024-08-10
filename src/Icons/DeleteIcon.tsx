import { FC } from "react";
import { SvgComponentProps } from "./TypeIcon";

export const DeleteIcon: FC<SvgComponentProps> = ({
  height,
  width,
  color = "#000",
  fill = "none",
  ...props
}) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={height}
    height={width}
    fill={fill}
    viewBox="0 0 24 24"
    {...props}
  >
    <path
      stroke={color}
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M10 11v6M14 11v6M4 7h16M6 7h12v11a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3V7ZM9 5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2H9V5Z"
    />
  </svg>
);
