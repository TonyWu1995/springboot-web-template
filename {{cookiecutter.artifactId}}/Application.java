package {{cookiecutter.__package}};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{ cookiecutter.applicationName }} {

    public static void main(String[] args) {
        SpringApplication.run({{ cookiecutter.applicationName }}.class, args);
    }

}
