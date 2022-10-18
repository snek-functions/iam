import cors from "cors";
import getServerlessApp from "@snek-at/functions/dist/server/getServerlessApp.js";

import { ConfigureApp } from "@snek-at/functions";

export async function handler(event: Object, context: Object) {
  return await getServerlessApp({
    functions: ".",
  })(event, context);
}

export const configureApp: ConfigureApp = (app) => {
  app.use((req, res, next) => {
    return cors({
      origin: true,
      credentials: true,
    })(req, res, next);
  });
};

// SPDX-License-Identifier: (EUPL-1.2)
// Copyright © 2019-2022 snek.at
