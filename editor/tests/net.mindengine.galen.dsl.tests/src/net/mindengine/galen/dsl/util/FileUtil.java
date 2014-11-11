package net.mindengine.galen.dsl.util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class FileUtil {

  public static StringBuilder readFile(final String pFile) throws Exception {
    File bsCWT = new File(pFile);
    @SuppressWarnings("resource")
    BufferedReader reader = new BufferedReader(new FileReader(bsCWT));
    StringBuilder content = new StringBuilder();
    String line;
    while ((line = reader.readLine()) != null) {
      // add file line by line to StringBuiler
      content.append(line + "\n");
    }
    return content;
  }
}
